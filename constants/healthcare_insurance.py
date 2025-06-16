from typing import Dict
from constants.category_handler import CategoryHandler


class HealthcareInsuranceCategoryHandler(CategoryHandler):
    def get_label_ids(self) -> Dict[str, str]:
        return {
            "Bảo hiểm qua ngân hàng": "684aa05ba6c09251a3a09f44",
            "Chi phí": "684aa05ba6c09251a3a09f45",
            "Chăm sóc khách hàng": "684aa05ba6c09251a3a09f46",
            "Cơ sở vật chất": "684aa05ba6c09251a3a09f47",
            "Dịch vụ": "684aa05ba6c09251a3a09f48",
            "Hoạt động cộng đồng": "684aa05ba6c09251a3a09f49",
            "Hoạt động truyền thông": "684aa05ba6c09251a3a09f4a",
            "Hợp tác": "684aa05ba6c09251a3a09f4b",
            "Nhân sự": "684aa05ba6c09251a3a09f4c",
            "Quyền lợi": "684aa05ba6c09251a3a09f4d",
            "Rao vặt": "684aa05ba6c09251a3a09f4e",
            "So sánh với đối thủ": "684aa05ba6c09251a3a09f4f",
            "Sản phẩm": "684aa05ba6c09251a3a09f50",
            "Sự kiện": "684aa05ba6c09251a3a09f51",
            "Thương hiệu chung": "684aa05ba6c09251a3a09f52",
            "Tuyển dụng": "684aa05ba6c09251a3a09f53",
            "Tư vấn": "684aa05ba6c09251a3a09f54",
            "Điều khoản": "684aa05ba6c09251a3a09f55",
            "Ưu đãi": "684aa05ba6c09251a3a09f56",
            "Đề cập chung": "684aa05ba6c09251a3a09f57",
            "Thành tựu": "684aa05ba6c09251a3a09f58",
            "Ban lãnh đạo": "684aa05ba6c09251a3a09f59",
            "Cổ phiếu": "684aa05ba6c09251a3a09f5a",
            "Kết quả kinh doanh": "684aa05ba6c09251a3a09f5b",
            "Chất lượng": "684aa05ba6c09251a3a09f5c",
            "Nguồn gốc": "684aa05ba6c09251a3a09f5d",
            "Thông cáo báo chí": "684aa05ba6c09251a3a09f5e",
            "Minigame/ Livestream": "684aa05ba6c09251a3a09f5f",
            "Hoạt động tài trợ": "684aa05ba6c09251a3a09f60",
            "Nghiên cứu & phát triển": "684aa05ba6c09251a3a09f61",
            "Thủ tục hành chính": "684aa05ba6c09251a3a09f62",
            "Đánh giá": "684aa05ba6c09251a3a09f63",
            "Chuyên khoa": "684aa05ba6c09251a3a09f64"
        }

    def get_labels(self) -> Dict[str, str]:
        return {
            "Bảo hiểm qua ngân hàng": "Nội dung về các sản phẩm bảo hiểm được phân phối qua kênh ngân hàng (bancassurance): bảo hiểm nhân thọ, bảo hiểm phi nhân thọ. Quy trình mua bảo hiểm tại ngân hàng và ưu nhược điểm của kênh này.",
            "Chi phí": "Nội dung về chi phí điều trị, phí bảo hiểm, mức đóng phí, chi phí khám chữa bệnh. So sánh chi phí giữa các đơn vị, thắc mắc về mức phí hợp lý và minh bạch chi phí.",
            "Chăm sóc khách hàng": "Phản hồi về dịch vụ chăm sóc khách hàng: thái độ phục vụ của nhân viên y tế/bảo hiểm, tốc độ xử lý yêu cầu, chất lượng tư vấn và hỗ trợ khách hàng. Đánh giá về sự tận tâm trong chăm sóc.",
            "Cơ sở vật chất": "Đánh giá về cơ sở vật chất của bệnh viện, phòng khám, trung tâm y tế: trang thiết bị y tế, không gian khám chữa bệnh, điều kiện vệ sinh. Hiện đại hóa và đầu tư cơ sở hạ tầng.",
            "Dịch vụ": "Nội dung về các dịch vụ y tế và bảo hiểm được cung cấp: khám bệnh, chữa bệnh, bảo hiểm sức khỏe, dịch vụ hỗ trợ. Đánh giá chất lượng và sự đa dạng của dịch vụ.",
            "Hoạt động cộng đồng": "Các hoạt động vì cộng đồng của đơn vị y tế/bảo hiểm: khám bệnh từ thiện, tuyên truyền sức khỏe, chương trình CSR. Đóng góp cho sức khỏe cộng đồng và trách nhiệm xã hội.",
            "Hoạt động truyền thông": "Các hoạt động truyền thông, marketing, quảng bá thương hiệu của đơn vị y tế/bảo hiểm. Chiến dịch tuyên truyền về sức khỏe, giáo dục bảo hiểm và nâng cao nhận thức.",
            "Hợp tác": "Thông tin về các hoạt động hợp tác giữa các đơn vị y tế, bảo hiểm với nhau hoặc với đối tác khác. Liên kết mạng lưới, hợp tác chiến lược và quan hệ đối tác.",
            "Nhân sự": "Nội dung về đội ngũ nhân sự y tế và bảo hiểm: bác sĩ, điều dưỡng, nhân viên tư vấn. Đánh giá về trình độ chuyên môn, thái độ phục vụ và kinh nghiệm của nhân viên.",
            "Quyền lợi": "Thông tin về quyền lợi của người bệnh, người mua bảo hiểm: quyền lợi bảo hiểm, chế độ ưu đãi, quyền lợi khách hàng VIP. Giải thích về các quyền lợi được hưởng và điều kiện áp dụng.",
            "Rao vặt": "Các bài đăng rao vặt về dịch vụ y tế, bảo hiểm: quảng cáo cá nhân, chia sẻ thông tin liên hệ, trao đổi kinh nghiệm. Thông tin phi chính thức từ người dùng.",
            "So sánh với đối thủ": "Nội dung so sánh giữa các đơn vị y tế, công ty bảo hiểm về chất lượng dịch vụ, giá cả, quyền lợi. Phân tích ưu nhược điểm và vị thế cạnh tranh trên thị trường.",
            "Sản phẩm": "Thông tin về các sản phẩm bảo hiểm, gói khám chữa bệnh: đặc điểm sản phẩm, phạm vi bảo hiểm, điều kiện tham gia. Giới thiệu các sản phẩm mới và cải tiến sản phẩm.",
            "Sự kiện": "Thông tin về các sự kiện của đơn vị y tế/bảo hiểm: hội nghị khoa học, lễ khai trương, ngày hội sức khỏe. Tham gia và phản hồi về các sự kiện được tổ chức.",
            "Thương hiệu chung": "Đề cập tổng quát về thương hiệu đơn vị y tế/bảo hiểm mà không tập trung vào vấn đề cụ thể nào. Nhận xét chung về uy tín và vị thế trên thị trường.",
            "Tuyển dụng": "Thông tin về tuyển dụng nhân sự trong lĩnh vực y tế và bảo hiểm: vị trí tuyển dụng, yêu cầu công việc, chế độ đãi ngộ. Cơ hội nghề nghiệp và phát triển trong ngành.",
            "Tư vấn": "Đánh giá về chất lượng dịch vụ tư vấn y tế và bảo hiểm: tính chính xác của lời khuyên, sự hỗ trợ của tư vấn viên, khả năng giải đáp thắc mắc. Hiệu quả của việc tư vấn chuyên môn.",
            "Điều khoản": "Nội dung về các điều khoản, điều kiện của hợp đồng bảo hiểm, quy định khám chữa bệnh. Giải thích về các điều khoản quan trọng và quyền nghĩa vụ của các bên.",
            "Ưu đãi": "Thông tin về các chương trình ưu đãi, khuyến mãi: giảm phí bảo hiểm, ưu đãi khám chữa bệnh, quà tặng cho khách hàng. Điều kiện và thời gian áp dụng các ưu đãi.",
            "Đề cập chung": "Nội dung đề cập đến đơn vị y tế/bảo hiểm một cách chung chung, không cụ thể về dịch vụ hay vấn đề nào. Các bình luận ngắn gọn hoặc đề cập trong ngữ cảnh rộng.",
            "Thành tựu": "Nội dung về các thành tựu, giải thưởng, chứng nhận của đơn vị y tế/bảo hiểm. Công nhận về chất lượng dịch vụ, đạt chuẩn quốc tế và các thành tích đáng ghi nhận.",
            "Ban lãnh đạo": "Thông tin về ban lãnh đạo, CEO, giám đốc của đơn vị y tế/bảo hiểm. Chiến lược phát triển, tầm nhìn của lãnh đạo và thay đổi nhân sự cấp cao.",
            "Cổ phiếu": "Nội dung về cổ phiếu của công ty bảo hiểm, tập đoàn y tế trên thị trường chứng khoán. Phân tích giá cổ phiếu, triển vọng đầu tư và thông tin tài chính.",
            "Kết quả kinh doanh": "Thông tin về báo cáo tài chính, doanh thu, lợi nhuận của đơn vị y tế/bảo hiểm. Hiệu quả hoạt động kinh doanh và tăng trưởng của đơn vị.",
            "Chất lượng": "Đánh giá về chất lượng dịch vụ y tế và bảo hiểm: chất lượng khám chữa bệnh, hiệu quả điều trị, độ tin cậy của dịch vụ bảo hiểm. Tiêu chuẩn chất lượng và cải thiện liên tục.",
            "Nguồn gốc": "Thông tin về nguồn gốc, lịch sử hình thành và phát triển của đơn vị y tế/bảo hiểm. Truyền thống, giá trị cốt lõi và quá trình phát triển qua các thời kỳ.",
            "Thông cáo báo chí": "Các thông cáo báo chí chính thức của đơn vị y tế/bảo hiểm về các sự kiện quan trọng, thông tin mới. Công bố chính thức và thông tin đối với truyền thông.",
            "Minigame/ Livestream": "Các hoạt động minigame, livestream do đơn vị y tế/bảo hiểm tổ chức để tương tác với khách hàng. Chương trình giải trí kết hợp tuyên truyền sức khỏe.",
            "Hoạt động tài trợ": "Thông tin về các hoạt động tài trợ của đơn vị y tế/bảo hiểm: tài trợ sự kiện, nghiên cứu khoa học, hoạt động xã hội. Đầu tư cho cộng đồng và phát triển ngành.",
            "Nghiên cứu & phát triển": "Nội dung về hoạt động nghiên cứu và phát triển: nghiên cứu y khoa, phát triển sản phẩm bảo hiểm mới, ứng dụng công nghệ. Đầu tư cho innovation và cải tiến.",
            "Thủ tục hành chính": "Thông tin về các thủ tục hành chính liên quan đến khám chữa bệnh và bảo hiểm: giấy tờ cần thiết, quy trình làm việc, thủ tục thanh toán. Đơn giản hóa và cải thiện quy trình.",
            "Đánh giá": "Các ý kiến đánh giá tổng quan về dịch vụ y tế và bảo hiểm từ khách hàng. Phản hồi về trải nghiệm sử dụng dịch vụ, mức độ hài lòng và đề xuất cải thiện.",
            "Chuyên khoa": "Nội dung về các chuyên khoa y tế: tim mạch, ung bướu, nhi khoa, sản phụ khoa. Thông tin về năng lực chuyên môn, trang thiết bị và dịch vụ chuyên khoa."
        }

    def get_prompt_template(self) -> str:
        return """Bạn là một trợ lý phân loại nội dung trong lĩnh vực y tế và bảo hiểm, ngữ cảnh social listening. 
        Dựa trên văn bản sau, hãy chọn **một nhãn duy nhất** phù hợp nhất từ danh sách nhãn được cung cấp. 
        Trả về **chỉ nhãn** dưới dạng chuỗi JSON, ví dụ: {{"label": "Chăm sóc khách hàng"}}.

        **Văn bản**: {text}

        **Danh sách nhãn và mô tả**:
        {labels}
        """

    