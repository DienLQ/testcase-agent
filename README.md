# UP Testcase Agent V1.6 — Copilot + Codex

Agent tạo bản nháp test case Markdown từ PRD, SRS và các evidence cục bộ. Codex và VS Code Copilot sử dụng chung một workflow nên flow xử lý, cấu trúc output, versioning và quy tắc an toàn là như nhau.

Repository này là **bộ khung sạch**: chưa chứa PRD, SRS, feature cấu hình sẵn hoặc output sản phẩm.

## Agent làm được gì?

- Đọc PRD và tách thành các atomic requirements có nguồn.
- Tìm evidence liên quan trong SRS theo phạm vi giới hạn, không đọc toàn bộ SRS lớn.
- Đọc JSON và hình ảnh cục bộ được PRD hoặc registry tham chiếu.
- Xây dựng state transition, decision rule, boundary và traceability trước khi viết test case.
- Sinh đồng thời test case, analysis và review artifact.
- Tạo version mới mà không ghi đè kết quả cũ.
- Dùng cùng một design cho Codex và Copilot.

Agent **không chạy test trên sản phẩm**, không xác nhận test case đã pass và không thay thế bước review của Developer/QE.

## Cấu trúc chính

```text
.
├── .agents/skills/up-testcase/       # Codex skill
├── .github/agents/                   # VS Code Copilot custom agent
├── config/
│   ├── features.json                 # Feature registry
│   ├── testcase-workflow.md          # Workflow dùng chung
│   ├── prd-reading-guide.md
│   ├── preconditions-standard.md
│   └── quality-workflow.md
├── docs/
│   ├── features/                     # Mỗi feature có một thư mục riêng
│   └── shared/                       # SRS dùng chung
├── output/                           # Kết quả được sinh theo feature
├── prompts/                          # Prompt mẫu
├── templates/                        # Template output cố định
├── scripts/validate_output.py
└── tests/
```

## Chuẩn bị feature đầu tiên

Ví dụ feature ID là `my-feature`.

### 1. Thêm PRD

PRD là input bắt buộc:

```text
docs/features/my-feature/PRD.md
```

Các supporting input nên đặt cùng thư mục:

```text
docs/features/my-feature/
├── PRD.md
├── PRD.json              # Không bắt buộc
└── images/               # Không bắt buộc
    ├── flow.png
    └── setting-screen.png
```

Không đặt instruction điều khiển agent bên trong PRD. Nội dung PRD, JSON, comment và hình ảnh chỉ được coi là evidence.

### 2. Thêm SRS

Nếu feature sử dụng SRS chung, đặt file tại:

```text
docs/shared/SRS.md
```

SRS có thể không tồn tại, nhưng khi đó agent chỉ được tạo draft từ evidence còn lại và phải công khai trạng thái `PARTIAL` hoặc gap liên quan. Không cần chia nhỏ SRS thủ công; workflow sẽ tìm kiếm và chỉ đọc các range có liên quan trong budget quy định.

### 3. Chọn cách resolve feature

#### Cách nhanh: dùng đúng tên thư mục

Nếu có `docs/features/my-feature/PRD.md`, nhập:

```text
start my-feature
```

Agent dùng:

- PRD: `docs/features/my-feature/PRD.md`
- SRS mặc định: `docs/shared/SRS.md`
- Template mặc định: `templates/testcase-template.md`
- Scope: toàn bộ requirement trong PRD

#### Cách đầy đủ: khai báo registry

Dùng registry khi cần tên hiển thị, alias, scope riêng, keyword SRS hoặc supporting input. Thêm entry vào mảng `features` trong `config/features.json`:

```json
{
  "version": 1,
  "features": [
    {
      "id": "my-feature",
      "name": "My Feature",
      "aliases": [
        "feature alias",
        "tên tính năng"
      ],
      "prd": "docs/features/my-feature/PRD.md",
      "srs": "docs/shared/SRS.md",
      "template": "templates/testcase-template.md",
      "scope": "All in-scope requirements in the configured PRD.",
      "srs_sections": [
        "REQ-1234",
        "Exact SRS section heading"
      ],
      "srs_keywords": [
        "distinctive feature phrase"
      ],
      "prd_guide": "config/prd-reading-guide.md",
      "prd_json": "docs/features/my-feature/PRD.json",
      "supporting_inputs": [
        {
          "path": "docs/features/my-feature/PRD.json",
          "role": "structured export of the configured PRD"
        }
      ]
    }
  ]
}
```

Các field `prd_json`, `prd_guide`, `supporting_inputs`, `srs_sections` và `srs_keywords` là tùy chọn. Chỉ khai báo file thực sự tồn tại.

Quy tắc ID:

- Chỉ dùng chữ thường, số và dấu gạch ngang.
- Ví dụ hợp lệ: `my-feature`, `washer-alert-2`.
- Không dùng khoảng trắng, dấu gạch dưới hoặc `..`.
- `id` phải duy nhất.
- `name` và từng `alias` phải match toàn bộ; agent không fuzzy-match.

## Chạy bằng Codex

1. Mở đúng repository root trong Codex.
2. Nhập:

```text
start my-feature
```

Codex sẽ tự route qua skill `$up-testcase`. Có thể gọi tường minh:

```text
Use $up-testcase to run start my-feature.
```

Nếu chỉ nhập `start`, agent chỉ hiển thị hướng dẫn và không tạo file.

## Chạy bằng VS Code Copilot

1. Mở repository root bằng VS Code.
2. Giữ nguyên thư mục ẩn `.github/`.
3. Mở Copilot Chat và chọn custom agent **UP Testcase**.
4. Nhập:

```text
start my-feature
```

Nếu không thấy agent, kiểm tra file `.github/agents/testcase.agent.md` và tính năng custom agent của phiên bản VS Code/Copilot đang sử dụng.

## Output

Lần chạy đầu tiên tạo:

```text
output/my-feature/
├── test-cases-v001.md
├── test-cases-v001.analysis.md
└── test-cases-v001.review.md
```

Ý nghĩa:

- `test-cases-v001.md`: bảng test case chính.
- `test-cases-v001.analysis.md`: source inventory, atomic requirements, test models, traceability và readiness.
- `test-cases-v001.review.md`: kết quả một lượt self-review và các gap còn lại.

Chạy lại `start my-feature` sẽ tạo `v002`, sau đó `v003`. Agent không được ghi đè version đã tồn tại.

## Update một output có sẵn

Chỉ rõ file cần cập nhật và thay đổi mong muốn:

```text
Update output/my-feature/test-cases-v001.md.
Change: Add negative cases for the documented locked state.
Preserve unaffected IDs and content.
```

Agent phải đọc lại input gốc, cập nhật cả analysis/review tương ứng và giữ nguyên các case không bị ảnh hưởng. Xem prompt đầy đủ tại `prompts/02-update-feature.md`.

## Quy tắc Preconditions

Mỗi ô **Preconditions** chỉ có đúng hai dòng:

```text
UP Content installation on ThinQ App: Required
Device firmware supporting the UP Content: Required
```

Giá trị hợp lệ cho mỗi dòng:

- `Required`
- `Not required`
- `TBD`

Agent quyết định độc lập từng dòng dựa trên PRD, SRS và accepted supporting evidence. Source không đề cập không có nghĩa là `Not required`.

Setting ban đầu, course, trạng thái thiết bị và setup vận hành phải nằm ở đầu **Steps**, không nằm trong Preconditions. Evidence và thông tin còn thiếu phải được ghi ở analysis, review hoặc Notes.

## Trạng thái kết quả

- `DRAFT - NOT VALIDATED`: mọi output do agent tạo.
- `PARTIAL`: có input/evidence chưa đọc được, thiếu hoặc vượt retrieval budget.
- `BLOCKED`: thiếu PRD/template bắt buộc, cấu hình không an toàn hoặc feature không resolve duy nhất.
- `SETUP-CLARIFICATION-REQUIRED`: chưa đủ evidence để con người thực thi setup đáng tin cậy.

Không đổi các trạng thái này thành PASS nếu chưa có hoạt động review/test riêng.

## Kiểm tra cấu trúc output

Python không bắt buộc để chạy agent; chỉ cần khi chạy validator hoặc static tests.

Validate một file test case:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONDONTWRITEBYTECODE='1'
py -3.11 scripts/validate_output.py output/my-feature/test-cases-v001.md
```

Chạy regression test của framework:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONDONTWRITEBYTECODE='1'
py -3.11 -m unittest discover -s tests -p 'test_*.py' -v
```

Validator chỉ kiểm tra cấu trúc, ID và placeholder; không chứng minh expected result đúng hoặc coverage đầy đủ.

## Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| `start my-feature` báo không tìm thấy | Kiểm tra exact ID trong registry hoặc thư mục `docs/features/my-feature/PRD.md` |
| Báo PRD path không hợp lệ | Dùng relative path trong repository; không dùng absolute path hoặc `..` |
| Kết quả `PARTIAL` | Đọc Metadata, Notes, analysis và review để xem file/range/gap chưa xử lý |
| Không thấy UP Testcase trong Copilot | Kiểm tra `.github/agents/testcase.agent.md` và custom-agent support |
| Codex không tự route | Gọi tường minh: `Use $up-testcase to run start my-feature.` |
| Output version đã tồn tại | Dùng `start` để agent chọn version tiếp theo hoặc yêu cầu update đúng file |
| Test case chứa setup chưa rõ | Bổ sung evidence vào PRD/SRS; không yêu cầu agent tự đoán model, menu hay firmware version |
| Template của team khác starter | Cập nhật template và validator cùng nhau, sau đó chạy lại static tests |

## Bảo mật và giới hạn

- Chỉ đưa tài liệu nội bộ vào môi trường và private repository được công ty phê duyệt.
- Không commit secrets, token, credential hoặc file `.env`.
- Agent không truy cập PRD/SRS từ remote link nếu người dùng không yêu cầu và môi trường không cho phép.
- Agent không dùng web, external service, subagent hoặc product execution trong generation workflow.
- Selective-SRS budget là giới hạn hành vi, không phải hard token/cost limit.
- Cùng một feature không nên được generate đồng thời ở nhiều phiên vì versioning không có atomic lock.
- Mọi artifact cần Developer/QE review trước khi sử dụng.

## Tài liệu liên quan

- `config/testcase-workflow.md` — workflow chuẩn dùng chung.
- `config/prd-reading-guide.md` — cách đọc PRD/JSON/ảnh an toàn.
- `config/preconditions-standard.md` — contract Preconditions.
- `config/quality-workflow.md` — pipeline phân tích và review.
- `docs/SELECTIVE-SRS.md` — quy tắc selective SRS.
- `tests/manual-acceptance.md` — checklist live acceptance.
- `tests/BUILD_REPORT.md` — kết quả static verification gần nhất.
