import pandas as pd

# Tạo danh sách các tỉnh thành và khu vực lớn
province_data = {
    "province": [
        "Hà Nội", "Vĩnh Phúc", "Bắc Ninh", "Quảng Ninh", "Hải Dương", "Hải Phòng", 
        "Hưng Yên", "Thái Bình", "Hà Nam", "Nam Định", "Ninh Bình", 
        "Hà Giang", "Cao Bằng", "Bắc Kạn", "Tuyên Quang", "Lào Cai", "Yên Bái", 
        "Thái Nguyên", "Lạng Sơn", "Bắc Giang", "Phú Thọ", "Điện Biên", "Lai Châu", 
        "Sơn La", "Hòa Bình", 
        "Thanh Hóa", "Nghệ An", "Hà Tĩnh", "Quảng Bình", "Quảng Trị", 
        "Thừa Thiên Huế", "Đà Nẵng", "Quảng Nam", "Quảng Ngãi", "Bình Định", 
        "Phú Yên", "Khánh Hòa", "Ninh Thuận", "Bình Thuận", 
        "Kon Tum", "Gia Lai", "Đắk Lắk", "Đắk Nông", "Lâm Đồng", 
        "Bình Phước", "Tây Ninh", "Bình Dương", "Đồng Nai", 
        "Bà Rịa Vũng Tàu", "Hồ Chí Minh", 
        "Long An", "Tiền Giang", "Bến Tre", "Trà Vinh", "Vĩnh Long", 
        "Đồng Tháp", "An Giang", "Kiên Giang", "Cần Thơ", 
        "Hậu Giang", "Sóc Trăng", "Bạc Liêu", "Cà Mau"
    ],
    "region": [
        # Đồng bằng sông Hồng
        "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", 
        "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", 
        "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", 
        "Đồng bằng sông Hồng", "Đồng bằng sông Hồng", 
        # Trung du và miền núi phía Bắc
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        "Trung du và miền núi phía Bắc", "Trung du và miền núi phía Bắc", 
        # Bắc Trung Bộ và Duyên hải miền Trung
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung", 
        "Bắc Trung Bộ và Duyên hải miền Trung", "Bắc Trung Bộ và Duyên hải miền Trung",
        # Tây Nguyên
        "Tây Nguyên", "Tây Nguyên", "Tây Nguyên", "Tây Nguyên", "Tây Nguyên", 
        # Đông Nam Bộ
        "Đông Nam Bộ", "Đông Nam Bộ", "Đông Nam Bộ", "Đông Nam Bộ", 
        "Đông Nam Bộ", "Đông Nam Bộ", 
        # Đồng bằng sông Cửu Long
        "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", 
        "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", 
        "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", 
        "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", "Đồng bằng sông Cửu Long", 
        "Đồng bằng sông Cửu Long"
    ]
}

if __name__ == "__main__":
    # Tạo DataFrame từ dictionary
    province_df = pd.DataFrame(province_data)
    # Lưu DataFrame vào file CSV
    province_df.to_csv("province_region.csv", index=False)
