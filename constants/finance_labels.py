from typing import Optional, Dict, Any

from constants.category_handler import CategoryHandler

class FinanceCategoryHandler(CategoryHandler):
    """Handler for finance category classification."""
    
    def get_labels(self) -> Dict[str, str]:
        return {
            "Ad sales": "Nội dung quảng bá bán hàng, lời kêu gọi mua sản phẩm/dịch vụ.",
            "Brand mention": "Nội dung chỉ đơn thuần đề cập đến thương hiệu, không có cảm xúc rõ ràng hay ý định cụ thể.",
            "Counters/ Telesales": "Nội dung phản ánh về nhân viên tại quầy, telesales: gọi điện mời chào, tư vấn sản phẩm.",
            "Debt Issues": "Nội dung nói về việc nợ, trả nợ, chậm trả, khó khăn tài chính liên quan đến khoản vay.",
            "Fee/ Charge": "Phàn nàn, câu hỏi, hoặc thông tin liên quan đến phí dịch vụ, các khoản thu thêm.",
            "Harassment for Collection": "Phản ánh việc bị làm phiền do thu hồi nợ: gọi điện, nhắn tin, đe dọa.",
            "Harassment for Non Client": "Phản ánh bị làm phiền dù không phải khách hàng (gọi nhầm, spam).",
            "Harassment for Selling": "Phản ánh bị làm phiền vì mục đích bán hàng (quảng cáo, tiếp thị qua điện thoại).",
            "Harassment on Client's Relative": "Phản ánh việc làm phiền người thân của khách hàng về nợ, bán hàng, liên hệ gián tiếp.",
            "Interest": "Nội dung nói về lãi suất: cao, thấp, thay đổi, câu hỏi về mức lãi.",
            "Mobile app": "Đánh giá, phản ánh, hướng dẫn hoặc lỗi liên quan đến ứng dụng di động.",
            "Process/ Procedure": "Nội dung đề cập đến quy trình, thủ tục: mở tài khoản, vay vốn, thanh lý, v.v.",
            "Product information": "Câu hỏi, chia sẻ, mô tả về sản phẩm/dịch vụ đang được cung cấp.",
            "Recruitment/ Training": "Nội dung về tuyển dụng, đào tạo nhân viên, phỏng vấn, chia sẻ kinh nghiệm làm việc.",
            "Sellers/ Consultant": "Nội dung liên quan đến người bán hàng, tư vấn viên: thái độ, kiến thức, chăm sóc khách hàng.",
            "Terminate procedure": "Phản ánh hoặc hỏi về thủ tục chấm dứt dịch vụ, kết thúc hợp đồng, tất toán, đóng tài khoản.",
            "General mention": "Đề cập tổng quan về thương hiệu, không rõ vấn đề cụ thể.",
            "Staff attitude": "Nội dung nhận xét thái độ nhân viên: thân thiện, thô lỗ, hỗ trợ tốt/kém.",
            "Minigame/ livestream": "Nội dung liên quan đến mini game, livestream trên mạng xã hội hoặc kênh truyền thông.",
            "ESG": "Nội dung liên quan đến môi trường, xã hội, quản trị doanh nghiệp – ví dụ như hoạt động CSR.",
            "Promotion/ campaign": "Chia sẻ, thắc mắc hoặc phản ánh về chương trình khuyến mãi, ưu đãi, giảm giá.",
            "Achievement": "Nội dung ca ngợi, nêu thành tích thương hiệu (giải thưởng, xếp hạng, mốc tăng trưởng).",
            "Business result": "Thông tin, phân tích, báo cáo kết quả kinh doanh, doanh thu, lợi nhuận.",
            "Interactive posts": "Nội dung tương tác với người dùng: câu hỏi, bình chọn, trò chơi, lời kêu gọi tham gia hoạt động."
        }
    
    def get_label_ids(self) -> Dict[str, str]:
        return {
            "Ad sales": "675aa336e751a10ea07e70cf",
            "Brand mention": "5f473b1e5966faeb2259f5e4",
            "Counters/ Telesales": "5f473b0c5966faeb2259f5e3",
            "Debt Issues": "5f40d1cebc260e60500c2b86",
            "Fee/ Charge": "6088d05092f9ed4ad71d874a",
            "Harassment for Collection": "5f40d1f1bc260e60500c2b89",
            "Harassment for Non Client": "5f40d1d8bc260e60500c2b87",
            "Harassment for Selling": "5f40d1e3bc260e60500c2b88",
            "Harassment on Client's Relative": "60e7b3cddbc2292f90771652",
            "Interest": "6088d04692f9ed4ad71d8749",
            "Mobile app": "5f473ceba2d624f9dc50abfd",
            "Process/ Procedure": "675a88cde751a10ea07e70bd",
            "Product information": "675a88c7e751a10ea07e70bc",
            "Recruitment/ Training": "5f211c807e6e09dd8343b720",
            "Sellers/ Consultant": "5f473af05966faeb2259f5de",
            "Terminate procedure": "675aa2e4e751a10ea07e70ce",
            "General mention": "5f40cdd7bc260e60500c2af0",
            "Staff attitude": "5f40ce02bc260e60500c2af1",
            "Minigame/ livestream": "62cce32b33161b492fad9fcd",
            "ESG": "675a8910e751a10ea07e70c4",
            "Promotion/ campaign": "675a88d5e751a10ea07e70be",
            "Achievement": "682ee20f64598918c0f46f26",
            "Business result": "682ee22364598918c0f46f27",
            "Interactive posts": "682ee22864598918c0f46f28"
        }
    
    def get_prompt_template(self) -> str:
        return """Bạn là một trợ lý phân loại nội dung trong lĩnh vực tài chính, ngữ cảnh social listening. 
Dựa trên văn bản sau, hãy chọn **một nhãn duy nhất** phù hợp nhất từ danh sách nhãn được cung cấp. 
Trả về **chỉ nhãn** dưới dạng chuỗi JSON, ví dụ: {{"label": "Ad sales"}}.

**Văn bản**: {text}

**Danh sách nhãn và mô tả**:
{labels}
"""