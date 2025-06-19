from typing import Optional, Dict, Any

from constants.category_handler import CategoryHandler

class FinanceCategoryHandler(CategoryHandler):
    """Handler for finance category classification."""
    
    def get_labels(self) -> Dict[str, str]:
        return {
        "Ad sales": "Nội dung là để kêu gọi mọi người hãy vay tiền từ tổ chức tài chính. Mua hàng và thanh toán/ trả góp qua các công ty tài chính.",
        "Brand mention": "Nội dung chỉ đơn thuần đề cập đến thương hiệu, không có cảm xúc rõ ràng hay ý định cụ thể.",
        "Counters/ Telesales": "Nói về các telesales chuyên spam các cuộc gọi hoặc nhân viên tư vấn tại quầy.",
        "Debt Issues": "Nói về việc bùng các khoản nợ.",
        "Fee/ Charge": "Nói về các loại phí và các chi phí phát sinh, chi phí thay đổi trong quá trình vay.",
        "Harassment for Collection": "Nói về việc thu hồi các khoản nợ, quấy rầy để bắt khách trả nợ",
        "Harassment for Non Client": "Nói về việc bị làm phiền dù không phải khách hàng.",
        "Harassment for Selling": "Nói về việc bị làm phiền dù bản thân không phải là người vay.",
        "Harassment on Client's Relative": "Phản ánh việc làm phiền người thân của khách hàng về nợ, bán hàng, liên hệ gián tiếp.",
        "Interest": "Nội dung nói về lãi suất: cao, thấp, thay đổi, câu hỏi về mức lãi.",
        "Mobile app": "Đánh giá, phản ánh, hướng dẫn hoặc lỗi liên quan đến ứng dụng di động.",
        "Process/ Procedure": "Nói về các thủ tục vay vốn.",
        "Product information": "Câu hỏi, chia sẻ, mô tả về sản phẩm/dịch vụ đang được cung cấp.",
        "Recruitment/ Training": "Nội dung liên quan đến hoạt động tuyển dụng của công ty tài chính",
        "Sellers/ Consultant": "Nội dung liên quan đến người tư vấn bán hàng, tư vấn viên tại quầy hoặc qua điện thoại.",
        "Terminate procedure": "Nói về các thủ tục tất toán hợp đồng",
        "General mention": "Đề cập tổng quan về thương hiệu, không rõ vấn đề cụ thể.",
        "Staff attitude": "Nội dung nhận xét thái độ nhân viên: thân thiện, thô lỗ, hỗ trợ tốt/kém.",
        "Minigame/ livestream": "Nội dung liên quan đến mini game, livestream.",
        "ESG": "Nội dung liên quan đến môi trường, xã hội, quản trị doanh nghiệp – ví dụ như hoạt động CSR, tài trợ.",
        "Promotion/ campaign": "Nói về các hoạt động khuyến mãi giảm giá (không phải rao vặt) hoặc chiến dịch của brand có thể là nội bộ hoặc nhằm mục đích tăng nhận diện thương hiệu.",
        "Achievement": "Nói về thành tích thương hiệu (giải thưởng, xếp hạng, mốc tăng trưởng).",
        "Business result": "Thông tin, phân tích, báo cáo kết quả kinh doanh, doanh thu, lợi nhuận.",
        "Interactive posts": "Nội dung, bình luận chỉ mang tính tương tác, không mang bất cứ ý nghĩa gì, ví dụ như tag tên."
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