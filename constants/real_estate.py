from typing import Dict
from constants.category_handler import CategoryHandler


class RealEstateCategoryHandler(CategoryHandler):
    def get_label_ids(self) -> Dict[str, str]:
        return {
            "Giá": "68373c83584d853ca31a99dc",
            "Hoạt động cộng đồng": "68373c86584d853ca31a99dd",
            "Hoạt động kinh doanh": "68373c8d584d853ca31a99de",
            "Pháp lý": "68373c91584d853ca31a99df",
            "Rao vặt": "68373c96584d853ca31a99e0",
            "Sự kiện": "68373c9a584d853ca31a99e1",
            "Thiết kế": "68373c9f584d853ca31a99e2",
            "Thông tin dự án": "68373ca3584d853ca31a99e3",
            "Thông tin thị trường": "68373ca8584d853ca31a99e4",
            "Thương hiệu chung": "68373cac584d853ca31a99e5",
            "Tiến độ/ Bàn giao": "68373cb2584d853ca31a99e6",
            "Tiện ích": "68373cb6584d853ca31a99e7",
            "Tuyển dụng": "68373cbb584d853ca31a99e8",
            "Vị trí": "68373cbe584d853ca31a99e9",
            "Đề cập chung": "68373cc3584d853ca31a99ea",
            "Ban lãnh đạo": "68373cc8584d853ca31a99eb",
            "So sánh thương hiệu": "68373ccc584d853ca31a99ec",
            "Đơn vị thi công": "68373cd0584d853ca31a99ed",
            "An toàn xây dựng": "68373cd5584d853ca31a99ee",
            "Bài đăng quảng bá": "68373cda584d853ca31a99ef",
            "Hoạt động fanpage": "68373ce2584d853ca31a99f0",
            "Tiềm năng đầu tư": "68373ce6584d853ca31a99f1",
            "Minigame": "68373ceb584d853ca31a99f2",
            "Chất lượng": "68373cf3584d853ca31a99f3",
            "Chính sách mua bán": "68373cf7584d853ca31a99f4",
            "Vấn đề kỹ thuật": "68373cfb584d853ca31a99f5",
            "Cổ phiếu": "68373d01584d853ca31a99f6",
            "Chính sách bán hàng": "68373d05584d853ca31a99f7",
            "Hoạt động hợp tác": "68373d0a584d853ca31a99f8",
            "Hoạt động đầu tư": "68373d0e584d853ca31a99f9",
            "Kết quả kinh doanh": "68373d12584d853ca31a99fa",
            "Livestream": "684a9e7ea6c09251a3a09f42"
        }

    def get_labels(self) -> Dict[str, str]:
        return {
            "Giá": "Nội dung đề cập đến giá bán, giá thuê bất động sản. Bao gồm thông tin về mức giá, biến động giá, chính sách giá, so sánh giá với thị trường. Phản hồi về tính hợp lý của giá cả.",
            "Hoạt động cộng đồng": "Nội dung về các hoạt động cộng đồng, CSR, từ thiện, tài trợ do công ty bất động sản tổ chức. Đánh giá về trách nhiệm xã hội và đóng góp cho cộng đồng địa phương.",
            "Hoạt động kinh doanh": "Thông tin về các hoạt động kinh doanh chính của doanh nghiệp bất động sản: phát triển dự án, kinh doanh nhà đất, dịch vụ môi giới. Chiến lược kinh doanh và mở rộng thị trường.",
            "Pháp lý": "Nội dung về các vấn đề pháp lý liên quan đến bất động sản: thủ tục pháp lý, giấy phép xây dựng, sổ đỏ, tranh chấp pháp lý. Tuân thủ quy định của Nhà nước về bất động sản.",
            "Rao vặt": "Các bài đăng rao bán, cho thuê bất động sản. Thông tin liên hệ mua bán, trao đổi bất động sản. Nội dung quảng cáo cá nhân về giao dịch bất động sản.",
            "Sự kiện": "Thông tin về các sự kiện của công ty: lễ mở bán, lễ khai trương, sự kiện ra mắt dự án mới, lễ bàn giao. Tham gia và phản hồi về các sự kiện được tổ chức.",
            "Thiết kế": "Nội dung về thiết kế kiến trúc, nội thất, cảnh quan của dự án bất động sản. Đánh giá về tính thẩm mỹ, công năng sử dụng và xu hướng thiết kế hiện đại.",
            "Thông tin dự án": "Thông tin chi tiết về các dự án bất động sản: quy mô, loại hình, đặc điểm dự án. Giới thiệu về concept, mục tiêu và định hướng phát triển của dự án.",
            "Thông tin thị trường": "Chia sẻ về tình hình thị trường bất động sản, xu hướng phát triển, phân tích thị trường. Đánh giá về triển vọng và biến động của thị trường địa ốc.",
            "Thương hiệu chung": "Đề cập tổng quát về thương hiệu công ty bất động sản mà không tập trung vào vấn đề cụ thể nào. Nhận xét chung về uy tín, vị thế của công ty trên thị trường.",
            "Tiến độ/ Bàn giao": "Thông tin về tiến độ thi công, xây dựng dự án và việc bàn giao nhà cho khách hàng. Cập nhật về lịch trình hoàn thành và các milestone quan trọng của dự án.",
            "Tiện ích": "Nội dung về các tiện ích trong và ngoài dự án: hồ bơi, gym, công viên, trường học, bệnh viện. Đánh giá về chất lượng và sự đa dạng của tiện ích được cung cấp.",
            "Tuyển dụng": "Thông tin về tuyển dụng nhân sự trong ngành bất động sản: vị trí tuyển dụng, yêu cầu công việc, chế độ đãi ngộ. Chia sẻ kinh nghiệm làm việc trong lĩnh vực bất động sản.",
            "Vị trí": "Nội dung về vị trí địa lý của dự án bất động sản: khu vực, địa chỉ, kết nối giao thông, môi trường xung quanh. Đánh giá về tính thuận lợi và tiềm năng phát triển của vị trí.",
            "Đề cập chung": "Nội dung đề cập đến công ty bất động sản một cách chung chung, không cụ thể về dự án hay vấn đề nào. Thường là các bình luận ngắn gọn hoặc đề cập trong ngữ cảnh rộng hơn.",
            "Ban lãnh đạo": "Nội dung đề cập đến ban lãnh đạo, CEO, chủ tịch hội đồng quản trị của công ty bất động sản. Bao gồm thông tin về nhân sự cấp cao, chiến lược lãnh đạo, thay đổi nhân sự cấp cao.",
            "So sánh thương hiệu": "Nội dung so sánh giữa các thương hiệu bất động sản khác nhau về chất lượng, dịch vụ, giá cả. Đánh giá ưu nhược điểm của từng thương hiệu và vị thế cạnh tranh.",
            "Đơn vị thi công": "Thông tin về các đơn vị thi công, nhà thầu xây dựng dự án. Đánh giá về uy tín, chất lượng thi công và kinh nghiệm của đơn vị thực hiện dự án.",
            "An toàn xây dựng": "Nội dung về các biện pháp an toàn trong quá trình xây dựng, chất lượng công trình, tiêu chuẩn xây dựng. Cảnh báo và phòng ngừa rủi ro trong thi công.",
            "Bài đăng quảng bá": "Các bài viết, nội dung marketing, quảng cáo chính thức của công ty để giới thiệu dự án, thương hiệu. Chiến dịch truyền thông và hoạt động PR của doanh nghiệp.",
            "Hoạt động fanpage": "Nội dung và hoạt động trên các trang mạng xã hội chính thức của công ty. Tương tác với khách hàng, chia sẻ thông tin và cập nhật tin tức qua fanpage.",
            "Tiềm năng đầu tư": "Phân tích về tiềm năng đầu tư của dự án bất động sản: khả năng sinh lời, tăng giá, thanh khoản. Tư vấn về cơ hội đầu tư và rủi ro cần lưu ý.",
            "Minigame": "Các trò chơi nhỏ, gameshow, hoạt động giải trí do công ty tổ chức để tương tác với khách hàng. Chương trình khuyến mãi dưới hình thức trò chơi.",
            "Chất lượng": "Đánh giá về chất lượng xây dựng, hoàn thiện của dự án bất động sản. Phản hồi về độ bền, tính năng kỹ thuật và tiêu chuẩn chất lượng công trình.",
            "Chính sách mua bán": "Thông tin về các chính sách, điều kiện mua bán bất động sản của công ty: hỗ trợ vay vốn, thanh toán, bảo hành. Quy trình và thủ tục giao dịch mua bán.",
            "Vấn đề kỹ thuật": "Các vấn đề kỹ thuật phát sinh trong quá trình xây dựng hoặc sử dụng: lỗi thi công, sự cố kỹ thuật, bảo trì và sửa chữa. Giải pháp khắc phục các vấn đề kỹ thuật.",
            "Cổ phiếu": "Nội dung về cổ phiếu của công ty bất động sản trên thị trường chứng khoán: giá cổ phiếu, hiệu quả đầu tư, thông tin tài chính. Phân tích về triển vọng cổ phiếu ngành bất động sản.",
            "Chính sách bán hàng": "Các chính sách bán hàng, ưu đãi dành cho khách hàng: chiết khấu, quà tặng, chương trình khuyến mãi. Điều khoản và điều kiện áp dụng các chính sách bán hàng.",
            "Hoạt động hợp tác": "Thông tin về các hoạt động hợp tác với đối tác: liên doanh, liên kết, hợp tác phát triển dự án. Mạng lưới đối tác và quan hệ hợp tác chiến lược.",
            "Hoạt động đầu tư": "Nội dung về các hoạt động đầu tư của công ty: mua đất, phát triển dự án mới, mở rộng danh mục đầu tư. Chiến lược đầu tư và phân bổ nguồn lực.",
            "Kết quả kinh doanh": "Thông tin về báo cáo tài chính, doanh thu, lợi nhuận của công ty bất động sản. Phân tích hiệu quả hoạt động kinh doanh và tăng trưởng của công ty.",
            "Livestream": "Hoạt động livestream trực tuyến của công ty để giới thiệu dự án, tương tác với khách hàng, tư vấn bán hàng. Đánh giá về chất lượng và hiệu quả của các buổi livestream."
        }

    def get_prompt_template(self) -> str:
        return """Bạn là một trợ lý phân loại nội dung trong lĩnh vực bất động sản, ngữ cảnh social listening. 
        Dựa trên văn bản sau, hãy chọn **một nhãn duy nhất** phù hợp nhất từ danh sách nhãn được cung cấp. 
        Trả về **chỉ nhãn** dưới dạng chuỗi JSON, ví dụ: {{"label": "Vị trí"}}.

        **Văn bản**: {text}

        **Danh sách nhãn và mô tả**:
        {labels}
        """