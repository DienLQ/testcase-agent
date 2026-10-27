# V1.2 - Selective SRS retrieval

## Mục tiêu
Giữ `start <tên tính năng>` nhưng không đọc toàn bộ SRS lớn. Agent đọc PRD/template trước, tìm trong đúng file SRS rồi chỉ đọc các đoạn liên quan. Không có RAG, API riêng, terminal hoặc agent bổ sung.

## Giới hạn mặc định trong instruction
- Tối đa 6 lần tìm SRS; mỗi lần yêu cầu tối đa 20 vị trí khớp, 2 dòng context mỗi phía nếu tool hỗ trợ.
- Tối đa 12 lần đọc range, mỗi lần 200 dòng, tổng tối đa 2400 dòng được yêu cầu.
- Search snippets là context bổ sung, không nằm trong 2400 dòng range-read.
- Tính cả lần gọi thất bại và dependency; không reset ngân sách giữa chừng.
- Đây là giới hạn hành vi của model, KHÔNG phải hard limit token hoặc bảo đảm chi phí. Một dòng có thể rất dài. Không đo token thực tế trong package.
- Tool không hỗ trợ tìm/đọc có giới hạn: không đọc cả file để thay thế; báo giới hạn và tạo PARTIAL từ PRD nếu có thể.

## Cấu hình một lần
Mỗi entry trong `config/features.json` có thể khai báo `srs_sections` và `srs_keywords` bằng ID/heading và từ khóa thật của feature. Hai trường là tùy chọn; thiếu thì agent lấy hint từ PRD. Không dùng số dòng cố định làm mapping. Không attach toàn bộ SRS vào chat khi chạy.

Ví dụ entry minh họa (không phải requirement thật):

```json
{
  "id": "my-feature",
  "name": "Tính năng của tôi",
  "prd": "docs/features/my-feature/PRD.md",
  "srs": "docs/shared/SRS.md",
  "template": "templates/testcase-template.md",
  "srs_sections": ["REAL-REQ-ID", "Exact section heading"],
  "srs_keywords": ["Distinctive feature phrase"]
}
```

## Output và template cố định
Starter template có metadata về section/range đã đọc, counters và gaps. Không đổi cột test case. Nếu template thật không có chỗ ghi metadata, agent tạo file `<output-stem>.sources.md` bên cạnh. Nếu thiếu context, ghi PARTIAL/TBD; không tự bịa expected result. Giữ trạng thái DRAFT - NOT VALIDATED để validator starter hoạt động.

## Cập nhật workspace hiện có
1. Backup/commit workspace.
2. Thay `.github/agents/testcase.agent.md` bằng bản V1.2.
3. MERGE hai trường mapping vào entry thật trong `config/features.json`; không chép đè registry đang sử dụng.
4. Giữ nguyên PRD, SRS và template cố định của team trừ khi có kế hoạch migration đã được review.
5. Mở chat mới, chọn UP Testcase, nhập `start <tên tính năng>`.
6. Review tool calls: chỉ search đúng file SRS và read range; không đọc từ đầu đến cuối. Approval nền tảng vẫn áp dụng.

## Kiểm tra thực tế cần chạy
- Exact ID mapping: đọc đúng section và ghi nguồn.
- Mapping không có: tìm từ PRD, không đọc toàn file.
- Không tìm thấy: báo NOT RETRIEVED/PARTIAL, không khẳng định SRS không có requirement.
- Nhiều match/truncated: thu hẹp truy vấn, không paginate toàn bộ.
- Section lớn: chỉ đọc subsection trong budget, ghi phần bỏ sót.
- Dependency vòng: không đọc lặp vô hạn.
- Hết budget: dừng retrieval, PARTIAL/TBD.
- Update: cũng dùng selective retrieval, không đọc toàn SRS.
- Template team: giữ nguyên format, metadata vào chỗ có sẵn hoặc companion.

Chưa chạy live trong VS Code/Copilot và chưa có file SRS 178143 dòng của bạn. Các unit/static test không chứng minh model tuân thủ budget hoặc giảm token thực tế.
