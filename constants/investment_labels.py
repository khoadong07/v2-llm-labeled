from typing import Dict
from constants.category_handler import CategoryHandler


class InvestmentCategoryHandler(CategoryHandler):
    def get_label_ids(self) -> Dict[str, str]:
        return {
        "Ban lãnh đạo": "684aa711a6c09251a3a09f66",
        "Bảng giá / Bảng điện": "684aa71fa6c09251a3a09f67",
        "Chuyên gia phân tích": "684aa72ea6c09251a3a09f68",
        "Chăm sóc khách hàng": "684aa73ca6c09251a3a09f69",
        "Chứng quyền có đảm bảo": "684aa748a6c09251a3a09f6a",
        "Dịch vụ ngân hàng đầu tư": "684aa753a6c09251a3a09f6b",
        "Giao dịch điện tử": "684aa75ea6c09251a3a09f6c",
        "Hoạt động xã hội/ tài trợ": "684aa76fa6c09251a3a09f6d",
        "Khuyến mãi": "684aa77ba6c09251a3a09f6e",
        "Kết quả kinh doanh": "684aa784a6c09251a3a09f6f",
        "Margin": "684aa78fa6c09251a3a09f70",
        "Môi giới": "684aa79aa6c09251a3a09f71",
        "Phí giao dịch": "684aa7a4a6c09251a3a09f72",
        "Quan hệ nhà đầu tư": "684aa7afa6c09251a3a09f73",
        "Sự kiện": "684aa7bba6c09251a3a09f74",
        "Talkshow/ Hội thảo": "684aa7eca6c09251a3a09f75",
        "Thông tin thị trường": "684aa7f7a6c09251a3a09f76",
        "Thương hiệu chung": "684aa803a6c09251a3a09f77",
        "Thị phần": "684aa80ea6c09251a3a09f78",
        "Tuyển dụng nhân sự": "684aa819a6c09251a3a09f79",
        "Tư vấn": "684aa828a6c09251a3a09f7a",
        "Đề cập chung": "684aa834a6c09251a3a09f7b",
        "Uy tín thương hiệu": "684aa841a6c09251a3a09f7c",
        "Nền tảng & công nghệ giao dịch": "684aa84fa6c09251a3a09f7d",
        "Công cụ giao dịch & Dịch vụ cung cấp": "684aa85da6c09251a3a09f7e",
        "Phản hồi & đánh giá": "684aa86fa6c09251a3a09f7f",
        "M&A/ Tái cấu trúc": "684aa87ca6c09251a3a09f80",
        "Pháp lý/ Chính sách": "684aa886a6c09251a3a09f81",
        "Định giá / đầu tư tài sản": "684aa88ba6c09251a3a09f82",
        "Rủi ro & gian lận / Cảnh báo": "684aa890a6c09251a3a09f83",
        "Chứng chỉ quỹ": "684aa897a6c09251a3a09f84",
        "Tài khoản": "684aa89ca6c09251a3a09f85",
        "Cổ phiếu": "684aa8a2a6c09251a3a09f86",
        "Khả năng sinh lời": "684aa8a7a6c09251a3a09f87",
        "Vốn đầu tư": "684aa8ada6c09251a3a09f88",
        "Danh mục đầu tư": "684aa8b3a6c09251a3a09f89",
        "Phí quản lý": "684aa8b9a6c09251a3a09f8a"
    }

    def get_labels(self) -> Dict[str, str]:
        return {
        "Ban lãnh đạo": "Nội dung đề cập đến ban lãnh đạo, CEO, chủ tịch hội đồng quản trị, giám đốc điều hành của công ty chứng khoán/đầu tư. Bao gồm thông tin về nhân sự cấp cao, chiến lược lãnh đạo, thay đổi nhân sự cấp cao.",
        "Bảng giá / Bảng điện": "Nội dung liên quan đến bảng giá chứng khoán, bảng điện tử hiển thị giá cổ phiếu, thông tin về giá cả các sản phẩm đầu tư. Phản hồi về việc hiển thị giá, cập nhật giá real-time.",
        "Chuyên gia phân tích": "Nội dung đề cập đến các chuyên gia phân tích thị trường, báo cáo phân tích, dự báo thị trường, khuyến nghị đầu tư từ các chuyên gia. Đánh giá về chất lượng phân tích và dự báo.",
        "Chăm sóc khách hàng": "Phản hồi về dịch vụ chăm sóc khách hàng: thái độ phục vụ, tốc độ xử lý yêu cầu, chất lượng tư vấn, hỗ trợ kỹ thuật. Khiếu nại về dịch vụ CSKH hoặc khen ngợi về sự hỗ trợ tốt.",
        "Chứng quyền có đảm bảo": "Nội dung về sản phẩm chứng quyền có đảm bảo (CW): đặc điểm sản phẩm, cách thức giao dịch, rủi ro và lợi ích. Câu hỏi, thắc mắc về CW và kinh nghiệm đầu tư CW.",
        "Dịch vụ ngân hàng đầu tư": "Nội dung về các dịch vụ ngân hàng đầu tư: tư vấn M&A, phát hành trái phiếu, IPO, dịch vụ tài chính doanh nghiệp. Đánh giá về chất lượng dịch vụ ngân hàng đầu tư.",
        "Giao dịch điện tử": "Phản hồi về hệ thống giao dịch online: tính ổn định, tốc độ, giao diện người dùng, lỗi kỹ thuật. Kinh nghiệm sử dụng app/web giao dịch, đề xuất cải thiện tính năng.",
        "Hoạt động xã hội/ tài trợ": "Nội dung về các hoạt động CSR, tài trợ cộng đồng, từ thiện, hoạt động vì môi trường của công ty chứng khoán. Đánh giá về trách nhiệm xã hội của doanh nghiệp.",
        "Khuyến mãi": "Thông tin về các chương trình khuyến mãi: giảm phí giao dịch, ưu đãi cho khách hàng mới, quà tặng, chương trình tích điểm. Phản hồi về hiệu quả và thu hút của các chương trình khuyến mãi.",
        "Kết quả kinh doanh": "Thông tin về báo cáo tài chính, doanh thu, lợi nhuận của công ty chứng khoán. Phân tích hiệu quả hoạt động kinh doanh, tăng trưởng của công ty.",
        "Margin": "Nội dung về giao dịch ký quỹ (margin trading): điều kiện vay margin, lãi suất margin, rủi ro và lợi ích. Kinh nghiệm và thắc mắc về giao dịch margin.",
        "Môi giới": "Đánh giá về dịch vụ môi giới chứng khoán: chất lượng tư vấn từ nhân viên môi giới, phí môi giới, hỗ trợ giao dịch. Phản hồi về nhân viên môi giới và dịch vụ được cung cấp.",
        "Phí giao dịch": "Phản hồi về mức phí giao dịch chứng khoán: phí môi giới, phí chuyển khoản, các loại phí khác. So sánh phí giữa các công ty, thắc mắc về cơ cấu phí.",
        "Quan hệ nhà đầu tư": "Nội dung về hoạt động IR (Investor Relations): thông tin cổ đông, họp đại hội cổ đông, báo cáo định kỳ cho nhà đầu tư. Đánh giá về tính minh bạch thông tin.",
        "Sự kiện": "Thông tin về các sự kiện của công ty: khai trương chi nhánh, lễ kỷ niệm, sự kiện ra mắt sản phẩm mới. Tham gia và phản hồi về các sự kiện được tổ chức.",
        "Talkshow/ Hội thảo": "Nội dung về các chương trình talkshow tài chính, hội thảo đầu tư do công ty tổ chức. Đánh giá chất lượng nội dung, diễn giả và tính hữu ích của các buổi hội thảo.",
        "Thông tin thị trường": "Chia sẻ về tin tức thị trường chứng khoán, phân tích xu hướng, cập nhật diễn biến thị trường. Đánh giá về chất lượng thông tin thị trường được cung cấp bởi công ty.",
        "Thương hiệu chung": "Đề cập tổng quát về thương hiệu công ty chứng khoán mà không tập trung vào vấn đề cụ thể nào. Nhận xét chung về uy tín, vị thế của công ty trên thị trường.",
        "Thị phần": "Nội dung về thị phần của công ty chứng khoán trên thị trường: xếp hạng thị phần, tăng trưởng thị phần, so sánh với đối thủ cạnh tranh.",
        "Tuyển dụng nhân sự": "Thông tin về tuyển dụng: vị trí tuyển dụng, yêu cầu công việc, chế độ đãi ngộ. Chia sẻ kinh nghiệm phỏng vấn, môi trường làm việc tại công ty chứng khoán.",
        "Tư vấn": "Đánh giá về chất lượng dịch vụ tư vấn đầu tư: tính chính xác của lời khuyên, khả năng phân tích của tư vấn viên, sự hỗ trợ trong việc đưa ra quyết định đầu tư.",
        "Đề cập chung": "Nội dung đề cập đến công ty chứng khoán một cách chung chung, không cụ thể về dịch vụ hay vấn đề nào. Thường là các bình luận ngắn gọn hoặc đề cập trong ngữ cảnh rộng hơn.",
        "Uy tín thương hiệu": "Nội dung về danh tiếng, uy tín của công ty chứng khoán trên thị trường: giải thưởng nhận được, xếp hạng uy tín, đánh giá từ tổ chức độc lập về thương hiệu.",
        "Nền tảng & công nghệ giao dịch": "Đánh giá về nền tảng công nghệ, hạ tầng IT của hệ thống giao dịch: tính ổn định, bảo mật, tốc độ xử lý. Phản hồi về việc nâng cấp công nghệ và đổi mới kỹ thuật.",
        "Công cụ giao dịch & Dịch vụ cung cấp": "Nội dung về các công cụ hỗ trợ giao dịch: biểu đồ kỹ thuật, công cụ phân tích, tính năng đặt lệnh. Đánh giá về tính đa dạng và chất lượng của các dịch vụ được cung cấp.",
        "Phản hồi & đánh giá": "Các ý kiến phản hồi, đánh giá tổng quan về dịch vụ của công ty chứng khoán từ khách hàng. Bao gồm cả phản hồi tích cực và tiêu cực về trải nghiệm sử dụng dịch vụ.",
        "M&A/ Tái cấu trúc": "Thông tin về các hoạt động M&A (sáp nhập và mua lại), tái cấu trúc của chính công ty chứng khoán hoặc dịch vụ tư vấn M&A mà công ty cung cấp cho khách hàng doanh nghiệp.",
        "Pháp lý/ Chính sách": "Nội dung về các vấn đề pháp lý, tuân thủ quy định của Nhà nước, chính sách mới ảnh hưởng đến hoạt động của công ty chứng khoán. Thông tin về thay đổi quy định thị trường.",
        "Định giá / đầu tư tài sản": "Nội dung về dịch vụ định giá tài sản, định giá doanh nghiệp, tư vấn đầu tư vào các loại tài sản khác nhau. Phân tích về giá trị và tiềm năng của các khoản đầu tư.",
        "Rủi ro & gian lận / Cảnh báo": "Cảnh báo về các rủi ro đầu tư, gian lận tài chính, lời khuyên về quản lý rủi ro. Thông tin về các biện pháp bảo vệ nhà đầu tư và phòng chống gian lận.",
        "Chứng chỉ quỹ": "Nội dung về các sản phẩm chứng chỉ quỹ (fund certificates): đặc điểm sản phẩm, hiệu suất quỹ, phí quản lý. Kinh nghiệm đầu tư và đánh giá về các quỹ được phân phối.",
        "Tài khoản": "Vấn đề liên quan đến tài khoản giao dịch: mở tài khoản, thay đổi thông tin, bảo mật tài khoản, quy trình đóng tài khoản. Thắc mắc về điều khoản và điều kiện tài khoản.",
        "Cổ phiếu": "Nội dung về giao dịch cổ phiếu: mua bán cổ phiếu, phân tích cổ phiếu, thông tin về các mã cổ phiếu cụ thể. Chia sẻ kinh nghiệm đầu tư cổ phiếu và chiến lược giao dịch.",
        "Khả năng sinh lời": "Đánh giá về hiệu quả đầu tư, tỷ suất sinh lời của các sản phẩm đầu tư. So sánh lợi nhuận giữa các kênh đầu tư và phân tích yếu tố ảnh hưởng đến khả năng sinh lời.",
        "Vốn đầu tư": "Nội dung về nguồn vốn để đầu tư: yêu cầu vốn tối thiểu, cách thức huy động vốn, quản lý vốn đầu tư. Thắc mắc về điều kiện vốn và khả năng tài chính để tham gia đầu tư.",
        "Danh mục đầu tư": "Nội dung về xây dựng và quản lý danh mục đầu tư: phân bổ tài sản, đa dạng hóa rủi ro, chiến lược đầu tư. Tư vấn về cơ cấu danh mục phù hợp với mục tiêu đầu tư.",
        "Phí quản lý": "Thông tin về các loại phí quản lý: phí quản lý danh mục, phí lưu ký, phí dịch vụ. Phản hồi về mức phí và so sánh với các công ty khác trong ngành."
    }
    def get_prompt_template(self) -> str:
        return """Bạn là một trợ lý phân loại nội dung trong lĩnh vực đầu tư, ngữ cảnh social listening. 
        Dựa trên văn bản sau, hãy chọn **một nhãn duy nhất** phù hợp nhất từ danh sách nhãn được cung cấp. 
        Trả về **chỉ nhãn** dưới dạng chuỗi JSON, ví dụ: {{"label": "Môi giới"}}.

        **Văn bản**: {text}

        **Danh sách nhãn và mô tả**:
        {labels}
        """