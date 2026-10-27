# Nâng cấp V1.3
1. Backup/commit workspace.
2. Thay .github/agents/testcase.agent.md.
3. Thêm config/prd-reading-guide.md, config/quality-workflow.md và templates/analysis-template.md, templates/review-template.md.
4. Merge prd_json, prd_guide, supporting_inputs vào registry thật. Giữ mapping SRS cũ. Không chép đè PRD/SRS/template/registry đang sử dụng.
5. Review mapping theo template PRD thực tế. Mở chat mới, chọn UP Testcase, nhập start <tên tính năng>.

Output: test case + .analysis.md + .review.md, và .sources.md khi cần. Giữ template test case của team. Framework trống không chứa ảnh nội bộ hoặc PRD sản phẩm.

Đã implement instruction pipeline và templates, không phải parser/OCR engine độc lập. Ảnh cần tool/model thực sự xem được ảnh. Không tự giải mã base64; embedded image chưa có local file sẽ được báo gap. JSON lớn không đọc an toàn được thì PARTIAL. Không bật terminal/network. Ngân sách là instruction, không hard limit.

Phân tích/review có thể tăng token so với draft đơn giản. Không bảo đảm đúng/đủ, giảm token hay coverage 100%. Developer/QE review toàn bộ.

## Acceptance live: NOT RUN
- MD/JSON trùng nội dung: không tạo requirement trùng.
- Guide/placeholder: không biến thành requirement.
- Số ảnh thay đổi: inventory theo references, không hard-code.
- Ảnh thiếu/không đọc được/base64: PARTIAL, không giả vờ đã xem.
- Nguồn mâu thuẫn: giữ cả nguồn, TBD.
- Flow/table: có model và traceability tới case.
- Thiếu precision: không tự tạo +/-1.
- Generate lại: version mới cho toàn bộ artifacts.
- Update: giữ phần không ảnh hưởng và ID.
- Template team: không đổi cột/headings.
- SRS lớn: giữ selective retrieval V1.2.

Chưa chạy live trong Copilot hoặc với bộ PRD thật. Static tests không chứng minh chất lượng ngữ nghĩa hoặc model tuân thủ instruction.
