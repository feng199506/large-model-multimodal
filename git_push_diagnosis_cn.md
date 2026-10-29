# Git 推送失败诊断报告（large_model_multimodal_literature）

- 诊断时间：2026-10-29（本地时区 +0100）
- 仓库：`/root/large_model_multimodal_literature`
- 本轮操作范围：只读诊断 + 方案准备。**未**删除文献、**未**重写历史、**未**强推、**未**修改任何服务器配置、**未**重传大包。唯一新增文件为本报告。

---

## 0. 结论摘要

| 项 | 结论 |
|---|---|
| 远端是否已到达本地 HEAD | **否**。远端 `main` 仍是 `9bf4204`（first commit），本地 HEAD 是 `f2ebd3d`（2-nd commit），领先 1 个提交。 |
| “Everything up-to-date” 是否可信 | **不可信**。`git ls-remote` 与 GitHub API 两路独立查询都显示远端没有更新。 |
| 根因 | 待推送的**单个提交** `f2ebd3d` 新增 1,710 个文件，树内容约 9.01 GiB，打包后约 8.09 GiB。它同时触犯 GitHub 的两条**强制**限制：**单次推送 2 GB**、**单文件 100 MiB**（有 3 个文件超限）。 |
| 能否靠“再多提交几次”拆小 | **不能**。`f2ebd3d` 是一个提交，首次传输必须一次带上它引用的全部新对象。在它后面追加提交只会让包更大。 |
| 推荐方向 | Git 只保存脚本、元数据和带 SHA-256 的清单；PDF/PPTX 全文放到独立文件存储（见第 5 节方案 C）。在获得你确认之前，不做任何改写。 |

---

## 1. 工作区、分支与推送目标

| 项 | 值 |
|---|---|
| 当前分支 | `main` |
| upstream | `origin/main`（`branch.main.remote=origin`，`branch.main.merge=refs/heads/main`） |
| 实际 push remote | `origin` → `https://github.com/feng199506/large-model-multimodal.git`（URL 中**无**内嵌令牌，无需脱敏；`~/.git-credentials` 不存在，全局 gitconfig 为空） |
| 目标分支 | `refs/heads/main` |
| 本地 HEAD | `f2ebd3d5ff456952054dd4bb8ad88b7ec7bfe1a6`（“2-nd commit”，2026-10-29 15:28:32 +0100） |
| 本地 remote-tracking `origin/main` | `9bf420433de5ebc05c233f306c2f20a7c5a84402`（“first commit”，14:41:06 +0100） |
| 待推送提交数 | **1**（`git rev-list --count origin/main..HEAD` = 1；仓库总共 2 个提交） |
| 工作区未提交改动 | 29 个已修改文件 + 202 个未跟踪文件（未跟踪文件共约 1.07 GiB，其中 184 个在 `papers/`） |
| 客户端代理 / postBuffer | 无 `http(s)_proxy` 环境变量，无 `http.proxy`，无 `http.postBuffer` 设置 |
| Git 版本 / LFS | git 2.53.0；**未安装 git-lfs**；未安装 `gh`、`git-filter-repo` |

reflog 摘录：

```
f2ebd3d HEAD@{2026-10-29 15:28:32 +0100}: commit: 2-nd commit
9bf4204 HEAD@{2026-10-29 14:41:06 +0100}: Branch: renamed refs/heads/master to refs/heads/main
9bf4204 HEAD@{2026-10-29 14:41:06 +0100}: commit (initial): first commit
```

`origin/main` 的引用日志只有一条 `update by push`（`0000000 → 9bf4204`），即只有首个提交被成功推送过。

---

## 2. 远端同步状态（直接查询，不依赖本地 tracking 分支）

**① `git ls-remote origin`（直接查询推送目标）：**

```
9bf420433de5ebc05c233f306c2f20a7c5a84402	HEAD
9bf420433de5ebc05c233f306c2f20a7c5a84402	refs/heads/main
```

**② GitHub REST API（匿名，独立通道）：**

- `GET /repos/feng199506/large-model-multimodal`：`private: False`，`default_branch: main`，`pushed_at: 2026-10-29T13:41:10Z`（即 14:41 +0100，与首次提交推送时间一致）
- `GET /repos/.../commits/main`：`9bf420433de5ebc05c233f306c2f20a7c5a84402`

**判定：** 远端 `main` = `9bf4204`，本地 HEAD = `f2ebd3d`，**远端未更新**。需要推送 `f2ebd3d`（或它的替代方案）。

关于 “Everything up-to-date”：HTTP 推送在 send-pack 阶段被断开（HTTP 500 / unexpected disconnect）后，git 拿不到远端的 ref 更新状态报告，常会在结尾误打印这一行；也可能是之后对某个已同步的 ref 重新执行了 push。无论哪种原因，上面两路查询已经确认远端没有更新，**不应**把这行输出当作推送成功。

---

## 3. 对象库与提交内容统计

### 3.1 对象库

```
git count-objects -vH
count: 1834          # 全部为松散对象
size: 8.17 GiB
in-pack: 0 / packs: 0
```

`.git` 共 8.2 GB，工作区（不含 .git）11 GB，磁盘 `/` 剩余 119 GB（已用 74%）。

### 3.2 各提交的树大小

| 提交 | 文件数 | 树内容总大小 | 说明 |
|---|---:|---:|---|
| `9bf4204` first commit（已在远端） | 37 | ≈ 0.01 GiB | 含 4 个小 PDF（最大 9.38 MiB），另误收 2 个 `scripts/__pycache__/*.pyc` |
| `f2ebd3d` 2-nd commit（未推送） | 1,747 | **≈ 9.01 GiB** | 相对上一提交：新增 1,710 个文件，修改 18 个 |

PDF 基本已是压缩格式，zlib 几乎压不动：松散对象 8.17 GiB ≈ 推送日志里 8.09 GiB 的 pack。数字相互吻合。

### 3.3 按扩展名统计（`f2ebd3d` 树）

| 扩展名 | 文件数 | 大小 |
|---|---:|---:|
| pdf | 1,254 | **8.708 GiB** |
| pptx | 4 | 0.185 GiB |
| json | 83 | 0.033 GiB |
| gif | 11 | 0.024 GiB |
| png | 84 | 0.021 GiB |
| zip | 1 | 0.018 GiB |
| 其余（webp/html/css/字体等） | — | < 0.02 GiB |

### 3.4 按顶层目录统计

| 目录 | 文件数 | 大小 |
|---|---:|---:|
| `university_materials/` | 807 | ≈ 5.39 GiB |
| `papers/` | 495 | 2.84 GiB |
| `books/` | 374 | 0.74 GiB |
| `scripts/` | 71 | 0.03 GiB |

### 3.5 最大文件 / 最大历史 blob

整个历史只有 2 个提交，所以“最大历史 blob”就是 `f2ebd3d` 树里的最大文件。

**超过 100 MiB（GitHub 直接拒收）：**

| 字节数 | MiB | 路径 |
|---:|---:|---|
| 171,708,963 | 163.8 | `university_materials/Cornell_CS5788_2026Spring_LectureMaterials_en/lec18_diffusion_for_images_en.pdf` |
| 162,199,798 | 154.7 | `university_materials/Cornell_CS5788_2026Spring_LectureMaterials_en/lec23_provenance_en.pdf` |
| 151,421,194 | 144.4 | `books/Murphy_ProbabilisticMLAdvancedTopics_en.pdf` |

**50–100 MiB（GitHub 警告）：** 共 7 个，例如 `lec11_vondrick_generative_models_for_vision_en.pdf`（95.1 MiB）、`lect08_generative_adversarial_networks_en.pdf`（90.9 MiB）、`Sutton_ReinforcementLearningAnIntroduction_2ndEd_en.pdf`（69.7 MiB）、`10_jimfangr00t_en.pdf`（60.2 MiB）、`lecture14_energy_based_models_3_en.pptx`（56.3 MiB）、`Li_MultimodalFoundationModels_en.pdf`（55.5 MiB）、`Zhang_DaGuiMoYuYanMoXing_2ndEd_cn.pdf`（53.3 MiB）。

**判定：** PDF/PPTX 等二进制全文**直接进入了普通 Git 历史**。仓库没有 `.gitattributes`（无 LFS 规则），也没有 `.gitignore`。

---

## 4. 托管平台与官方限制

平台：**GitHub.com**（`github.com/feng199506/large-model-multimodal`，公开仓库）。以下限制均于 2026-10-29 从 GitHub 官方文档查得：

| 限制 | 官方值 | 来源 | 本次情况 |
|---|---|---|---|
| 单次推送大小 | “Push size: This limit is enforced at 2GB.” | Repository limits | 8.09 GiB，**约为上限 4 倍** |
| 单文件 | 超过 50 MiB 警告；“GitHub blocks files larger than 100 MiB.” | About large files on GitHub | **3 个文件超过 100 MiB**，7 个超过 50 MiB |
| 推荐仓库大小 | “ideally less than 1 GB, and less than 5 GB is strongly recommended”；`.git` 磁盘大小建议上限 10 GB | About large files / Repository limits | 若全部进入普通 Git，约 9–10 GB |
| 单目录条目 | 3,000 | Repository limits | 未超（`papers/` 约 680 个） |
| Git LFS 单文件上限 | Free/Pro 2 GB，Team 4 GB，Enterprise Cloud 5 GB | About Git Large File Storage | 最大文件 164 MiB，不受影响 |
| Git LFS 免费额度（个人 Free） | 存储 10 GiB、带宽 10 GiB/月；超额且未设付款方式时无法再推送新文件，或 LFS 在当月被禁用 | Git LFS billing | 二进制合计约 8.9 GiB + 未跟踪 1.07 GiB ≈ **9.9 GiB，基本占满**；完整克隆一次就会耗掉约一个月的带宽 |
| Release 附件 | 单文件 < 2 GiB；每个 release 最多 1000 个附件；“no limit on the total size of a release, nor bandwidth usage” | About releases | 可用于方案 C |

文档链接：
- https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- https://docs.github.com/en/billing/concepts/product-billing/git-lfs
- https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

---

## 5. 服务端日志与资源

远端是 GitHub.com 托管服务，**没有任何服务端访问权限**：无法查看这次请求对应的 Git 服务日志、反向代理日志、服务器磁盘、超时设置或请求体上限。本机客户端侧也没有配置代理或 postBuffer，可以排除本地代理截断。

根据官方文档里的强制限制（2 GB 推送 + 100 MiB 文件）与 8.09 GiB 包体的对应关系，HTTP 500 / unexpected disconnect 已能得到充分解释，不需要服务端日志也能定性。剩余待查项：GitHub 对超过 2 GB 的推送在 HTTP 层具体返回什么（是 500 还是连接被重置），文档没有写明。这一点不影响修复方案。

---

## 6. 根因

1. **单次推送超限（主因）：** `f2ebd3d` 一个提交引入约 9 GiB 新对象，打包后 8.09 GiB，超过 GitHub 强制的 2 GB 推送上限，服务端在接收过程中中断（HTTP 500 / unexpected disconnect）。
2. **单文件超限（即使把包拆小也会失败）：** 3 个 PDF 超过 100 MiB，GitHub 的 pre-receive 检查会拒收任何包含它们的推送。
3. **结构性问题：** 约 8.9 GiB 二进制全文直接进入普通 Git 历史，远超 GitHub 推荐的 1 GB / 5 GB 仓库大小。工作区还有 1.07 GiB 未跟踪 PDF 等待加入。

**关于“拆分推送”的说明：** 待推送的只有 1 个提交，**不存在可以逐个推送的中间提交**。在 `f2ebd3d` 后面继续追加提交，不会让 `f2ebd3d` 的首次传输变小。要分批推送，只能把 `f2ebd3d` 替换为一串新的小提交。`f2ebd3d` 从未到达远端，所以替换它**不需要强推**，但这在本地仍然属于改写历史，需要你确认后才执行。

**关于 LFS 的说明：** 只新增 `.gitattributes` 跟踪规则，**不会**让 `f2ebd3d` 里已有的普通 blob 变小。必须用 `git lfs migrate import` 改写 `f2ebd3d`，才能把这些文件变成 LFS 指针。

---

## 7. 修复方案（均未执行，等待你选择）

### 第 0 步：通用前置（所有方案都要先做；非破坏性）

```bash
cd /root/large_model_multimodal_literature
# 1) 用引用钉住现有提交，任何后续操作都可以回到它
git branch backup/f2ebd3d-full f2ebd3d
git tag    backup-f2ebd3d-20261029 f2ebd3d

# 2) 生成全量 SHA-256 清单（含未跟踪文件），保存目录结构、文件大小和校验值
#    读取约 10 GB；本机有生产服务，用低优先级运行
find . -path ./.git -prune -o -type f -print0 \
  | sort -z \
  | nice -n 19 ionice -c3 xargs -0 sha256sum > ../lmml_sha256_manifest_en.txt
find . -path ./.git -prune -o -type f -printf '%s\t%p\n' | sort -k2 > ../lmml_size_manifest_en.tsv

# 3) 记录 Git blob 编号（零额外 IO，可与 SHA-256 清单交叉核对）
git -c core.quotepath=false ls-tree -r -l f2ebd3d > ../lmml_git_tree_f2ebd3d_en.tsv
```

另建议补一个 `.gitignore`，至少加入 `__pycache__/` 和 `*.pyc`（首个提交里误收了 2 个 `.pyc`）。

### 方案 C（推荐）：Git 只存文本和清单，全文放独立存储

**适用：** 希望 GitHub 仓库保持小巧、克隆快，同时完整保留全部文献。

1. 从 `origin/main` 新建分支，提交 `scripts/`、`domains/`、各种 `*_en.json` / `*_cn.json` / `*.md` 元数据，以及第 0 步生成的清单（清单要扩展字段：`路径 / 字节数 / sha256 / 存储位置`）。PDF、PPTX、ZIP、大图片写入 `.gitignore`。新分支预计只有几十 MB，可一次推送。
2. 全文二选一：
   - **GitHub Releases：** 按目录打成**不压缩**的 tar 包（`tar --format=posix -cf`，保留目录结构，文件字节不变），每个包控制在 1.5 GiB 以内（例如 `university_materials/` 按课程分组，`papers/`、`books/` 各分 2–3 包）。每个包和包内每个文件的 sha256 都写入清单，然后作为 release 附件上传。附件单个 < 2 GiB，总量和带宽不限。
   - **自有对象存储 / NAS / 网盘：** 用 `rsync -a --checksum` 或 `rclone copy --checksum` 同步，目录结构原样保留，清单里记录存储位置。
3. 恢复验证：在新目录克隆仓库 → 下载并解包 → `sha256sum -c lmml_sha256_manifest_en.txt` 全部 OK 后才算完成。
4. `f2ebd3d` 继续由 `backup/` 分支和 tag 保留在本地，直到第 3 步验证通过。

**注意：** 仓库当前是**公开**的，且包含整本出版教材（如 Murphy、Sutton、Zhang 等著作）和各校课件。无论选哪个方案，都建议先把仓库或 release 设为私有，或改放私有存储，避免版权问题（DMCA 下架会影响整个仓库）。

### 方案 B：Git LFS

**适用：** 坚持“git clone 即可拿到全文”，并且接受付费额度。

- 前提核实：需安装 git-lfs（本机未安装）。存储约 9.9 GiB，正好压在 Free 的 10 GiB 上限；带宽 10 GiB/月，完整克隆一次就耗尽。公开仓库被他人克隆，同样消耗你的配额。**需要先在 GitHub Billing 设置预算或购买额度。**
- 步骤（只改写未推送的 `f2ebd3d`，已在远端的 `9bf4204` 不动，因此不需要强推）：
  ```bash
  git lfs install --local
  git lfs migrate import --include="*.pdf,*.pptx,*.zip" --include-ref=refs/heads/main --exclude-ref=refs/remotes/origin/main
  git lfs ls-files | wc -l                  # 核对数量 ≈ 1,259
  git push origin main                      # LFS 对象经 LFS API 单独上传；Git 包只含指针，体积很小
  ```
- 验证：`git ls-remote` 比对提交号；新目录 `git clone` 后运行 `sha256sum -c`。

### 方案 A：普通 Git 分批推送（不推荐，列出供对比）

- 3 个超过 100 MiB 的文件**无论如何**进不了普通 Git，必须另存（方案 C 的方式）或走 LFS。不能为了缩小体积去重新压缩 PDF，否则校验值会变。
- 其余约 8.55 GiB，需从 `origin/main` 重新按目录建立 ≥ 6 个提交（每个 ≤ 1.5 GiB），然后逐个推送并逐个核对：
  ```bash
  git push origin <批次提交SHA>:refs/heads/main
  git ls-remote origin refs/heads/main      # 每推一批核对一次
  ```
- 推完后远端 `.git` 约 9 GB，接近 GitHub 推荐上限 10 GB，以后每次克隆都要下载约 9 GB。之后新增的文献会继续让仓库增大，而且无法缩回。

---

## 8. 待你决定的事项

1. 选择方案 C / B / A（建议 C）。
2. 仓库是否改为私有（建议是）。
3. 方案 C 下全文的存放位置：GitHub Releases，还是自有存储。
4. 是否允许执行第 0 步（建立 backup 引用 + 生成 SHA-256 清单；不删除、不改写任何内容）。

在你确认之前，`f2ebd3d` 保持原样，不会再尝试推送。

---

## 附：本次诊断执行的命令（均为只读）

```
git status -sb / git status --porcelain / git branch -vv / git remote -v / git config --get-regexp
git reflog / cat .git/logs/refs/remotes/origin/main
git rev-list --count origin/main..HEAD / git rev-parse HEAD origin/main
git ls-remote origin
git count-objects -vH / du -sh .git / df -h /root
git ls-tree -r -l 9bf4204 | f2ebd3d （按扩展名、目录、大小统计）
git diff --name-status 9bf4204 f2ebd3d
curl https://api.github.com/repos/feng199506/large-model-multimodal[/commits/main]
GitHub 官方文档（见第 4 节链接）
```
