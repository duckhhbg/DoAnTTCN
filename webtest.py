import streamlit as st
import pickle
import numpy as np

load = pickle.load(open('model_Random_Forest.sav','rb'))

def main():
    duan = ['Le Grand Jardin Sài Đồng', 'Golden Palace',
        'Vinhomes Ocean Park Gia Lâm', 'Tecco Garden',
        'Moonlight 1 - An Lạc Green Symphony', 'Hoàng Thành Pearl',
        'Masteri West Heights', 'Moonlight I - An Lạc Green Symphony',
        'Sunshine City', 'Sunshine Garden', 'Park Kiara', 'The Manor',
        'Discovery Complex', 'N01-T7 Ngoại Giao Đoàn', 'Feliz Homes',
        'Xuân Mai Complex', 'Gemek Premium', 'Golden Park Tower',
        'The Tonkin - Vinhomes Smart City', 'Vinhomes Green Bay Mễ Trì',
        'Vinhomes Metropolis - Liễu Giai', 'Vinhomes Gardenia',
        'Bắc Hà Fodacon', 'The Sakura - Vinhomes Smart City',
        'Vinhomes Skylake', 'Rose Town', 'Goldmark City', '6th Element',
        'Ciputra Hà Nội', 'The Emerald', 'An Lạc Green Symphony',
        'Mulberry Lane', 'Hyundai Hillstate', 'GoldSeason',
        'Udic Westlake', 'Park View City', 'N05 Trần Duy Hưng',
        'Riverside Garden', 'Mandarin Garden', 'Sunshine Center',
        'Mailand Hanoi City', 'Osaka Complex', 'BRG Diamond Residence',
        'KĐT Trung Văn - Vinaconex 3', 'Chelsea Park',
        'Tháp doanh nhân Tower', 'The Zenpark', 'D’. Le Roi Soleil ',
        'Grand Sunlake', 'Nam Trung Yên', 'Kim Văn Kim Lũ',
        'Hateco Laroma', 'FLC Complex Phạm Hùng', 'Imperia Smart City',
        'Sài Đồng', 'Bình Minh Garden', 'Geleximco Southern Star',
        'KĐT Xa La', 'Eco Lake View', 'KĐT Định Công', 'The Terra An Hưng',
        'Newtatco Complex', 'Mỹ Đình Plaza 2', 'Iris Garden',
        'Vinhomes Nguyễn Chí Thanh', 'CT3 Tây Nam Linh Đàm',
        'KĐT Linh Đàm', 'The Pavilion - Vinhomes Ocean Park',
        'Golden Land', 'HPC Landmark 105', 'Green Stars', 'KĐTM Cầu Bươu',
        'Discovery Central', 'Đại Thanh', 'Imperia Sky Garden',
        'An Bình City', 'Làng Việt Kiều Châu Âu Euroland',
        'Sun Grand City', 'The Nine', 'Căn hộ Thông tấn xã',
        'The Garden Hills - 99 Trần Bình', 'Dolphin Plaza',
        'Thăng Long Number One', 'K35 Tân Mai', 'Mỹ Đình I',
        'Eco City Việt Hưng', 'Green Diamond 93 Láng Hạ',
        'Ecolife Capitol', 'Eurowindow River Park', 'Kosmo Tây Hồ',
        'Mỹ Đình Pearl', 'Helios Tower 75 Tam Trinh',
        'Trung Hòa Nhân Chính', 'Rivera Park Hà Nội',
        'Trung tâm thương mại Chợ Mơ', 'Tràng An Complex',
        'The Matrix One', 'HC Golden City', 'Green Park Trần Thủ Độ',
        'Royal City', 'Times City', 'Times City - Park Hill',
        'MHD Trung Văn', 'Roman Plaza', 'Việt Hưng',
        '170 Đê La Thành - GP Building', 'South Building', 'Tứ Hiệp Plaza',
        'Berriver Long Biên', 'Bamboo Airways Tower', 'Ecohome Phúc Lợi',
        'Vinhomes Symphony Riverside', 'Cowaelmic 198 Nguyễn Tuân',
        'The Zurich - Vinhomes Ocean Park', 'The Pride', 'ĐTM Dịch Vọng',
        '137', 'Vinhomes Times City - Park Hill', 'Việt Đức Complex',
        'Thăng Long Capital', 'Seasons Avenue', 'Hinode City',
        'The Golden Palm Lê Văn Lương', 'KĐT Tây Hồ Tây - Starlake Hà Nội',
        'D’. Le Pont D’or - Hoàng Cầu', 'Keangnam',
        'Sky City Towers-88 Láng Hạ', 'The K Park', 'KĐT Văn Phú',
        'D22 Bộ Tư Lệnh Biên Phòng', 'Rice City Linh Đàm',
        'Eco Green City', 'Thống Nhất Complex', 'A10-A14 Nam Trung Yên',
        'Vinhomes Smart City', 'The Park Home', 'T&T Riverview', 'Ngõ 66',
        'Chung cư Ban cơ yếu Chính phủ', 'Văn Khê', 'Indochina Plaza',
        'Gemek Tower', 'Anland Complex', 'Vinhomes Smart City ',
        'Imperia Garden', 'Trung tâm Tài chính Sông Đà',
        'Golden Land - 275 đường Nguyễn Trãi', 'Hồ Gươm Plaza', 'Ngõ 169',
        'Hòa Bình Green City', 'Lancaster Hà Nội', 'Sky Park Residence',
        'KĐT Cổ Nhuế', 'Mipec Rubik 360', '25 Tân Mai',
        'N3 Đường Nguyễn Công Trứ', 'Sudico Mỹ Đình',
        '789 Bộ Tổng Tham Mưu - BQP', 'Hanhomes Blue Star', 'Sails Tower',
        'Florence Mỹ Đình', 'The Miami', 'Trung Yên Plaza',
        'Làng Quốc tế Thăng Long', 'Khai Sơn City', 'Thanh Hà Mường Thanh',
        'Hapulico Complex', 'Viễn Đông Star', 'Sky Central',
        'Diamond Park Plaza ', 'KĐTM Dương Nội', 'The Sparks',
        '93 Lò Đúc - Kinh Đô Tower', 'La Casta Văn Phú',
        'Chung cư Xuân La', 'Golden Westlake', 'Phương Đông Green Home',
        'Gelexia Riverside', 'Chung cư Đại Thanh', 'The Zei Mỹ Đình',
        'Eco Dream', 'Đồng Phát Park View Tower', 'Bea Sky',
        'An Bình Plaza', 'Home City - Trung Kính Complex', 'Sun Square',
        'Hateco Apollo', 'Thanh Bình Garden', '90 Nguyễn Tuân',
        'Cầu Giấy Center Point', 'KĐT Đại Kim', 'Hồng Hà Eco City',
        'Trinity Tower', 'The Link 345-CT1', 'Resco Cổ Nhuế',
        'BRG Grand Plaza', 'Tecco Diamond', 'Hà Nội Melody Residences',
        'C14 - Bộ Công An', 'Đặng Xá 1', 'TSG Lotus Sài Đồng',
        'Hei Tower Điện Lực', 'N03-T2 Ngoại Giao Đoàn', 'Usilk City',
        'Green Park CT15 Việt Hưng', 'The One Residence - Gamuda Garden',
        'Lavender Garden', 'Chung cư Viện 103', 'Mon City - Hải Đăng City',
        'Golden Field Mỹ Đình', 'Star Tower', 'Viện bỏng Lê Hữu Trác',
        'Home City Trung Kính', 'CT36 - Dream Home', 'HH1 Linh Đàm',
        'Star Tower 283 Khương Trung', 'Thanh Xuân Complex',
        "Vinhomes D'Capitale", 'Hà Nội Center Point',
        'Legend Tower 109 Nguyễn Tuân', '310 Minh Khai',
        'Tây Nam Đại học Thương Mại', 'Harmony Square',
        'Vinhomes West Point', 'Chung cư 122 Vĩnh Tuy',
        'Sunshine Riverside', 'B.I.G Tower', 'Dream Town', 'Ngõ 81',
        'Grandeur Palace', 'CT2 Xuân Phương',
        'Park Hill Premium - Times City', 'Sông Hồng Park View',
        'Tây Hồ Residence', 'N04B Ngoại Giao Đoàn', 'Dreamland Bonanza',
        'xpHOMES', 'The Park Home ', 'Xuân Mai Sparks Tower',
        'Số 9A ngõ 252/53', 'BID Residence', 'Sông Đà Hà Đông Tower',
        'CT2 Trung Văn Viettel Hancic', 'Samsora Premier',
        'South Tower Hoàng Liệt', 'Eurowindow Multi Complex',
        'Park View Residence', 'ngõ 7 Phố Thái Hà',
        'Tòa Tháp Thiên Niên Kỷ - Hatay Millennium', 'HH3 Linh Đàm',
        'ICID Complex', 'Phenikaa Hòa Lạc', 'Khu nhà ở Hưng Thịnh',
        'Tòa Tháp Thiên Niên Kỷ', 'Khu Ngoại Giao Đoàn',
        'The Golden An Khánh 32T', 'SDU 143 Trần Phú',
        'Xuân Mai Riverside', '54 Hạ Đình', 'Hà Nội Aqua Central',
        'B. I. G Tower', 'Sky Light', 'Mỹ Đình Plaza',
        'M3 - M4 Nguyễn Chí Thanh', 'VP3 Linh Đàm', 'Pháp Vân Tứ Hiệp',
        'VP6 Linh Đàm', 'Epic Tower', 'Momota Nguyễn Đức Cảnh',
        'The Golden Armor', 'Hà Nội Homeland', 'Mipec Riverside', 'Số 116',
        'Văn Phú Victoria', 'HH2 Linh Đàm', 'Mipec City View',
        'Khu đô thị mới Dịch Vọng', 'Ecohome 3', 'Mỹ Đình II',
        'N01-T4 Ngoại Giao Đoàn', 'Newtatco Vĩnh Phúc', 'Intracom1',
        'Vườn Xuân - 71 Nguyễn Chí Thanh', 'Hà Nội Paragon',
        'Startup Tower', 'Vinaconex 1', 'N04 Trần Duy Hưng',
        'CT2 Trung Văn - Vinaconex 3', '173 Xuân Thủy', 'New Skyline',
        'Nam Đô Complex', 'Tái định cư C18 Xuân La', 'The Vesta',
        'Ngõ 199', 'Imperial Plaza', 'Yên Hòa', 'Vimeco I - Phạm Hùng',
        'Hồng Hà Tower', 'Đông Nam Trần Duy Hưng', 'Five Star Kim Giang',
        'Nhà ở xã hội Him Lam Thượng Thanh', 'B1-B2 Tây Nam Linh Đàm',
        'FLC Green Apartment', 'Hoa Dao Hotel',
        'Artex Building 172 Ngọc Khánh', 'KĐT Làng Quốc tế Thăng Long',
        'King Palace', 'FLC Landmark Tower', 'IA20 Ciputra',
        'Nhà ở cho CBCS Bộ Công an', 'Green Pearl 378 Minh Khai',
        'Mandarin Garden 2', 'Heritage West Lake',
        'The Two Residence - Gamuda Garden', 'Chung cư 789 Xuân Đỉnh',
        '187 Tây Sơn', 'Thành Phố Giao Lưu', 'Vinata Tower',
        '671 Hoàng Hoa Thám', 'One 18 Ngọc Lâm', 'N01-T1 Ngoại Giao Đoàn',
        'Watermark Tây Hồ', 'C37 Bộ Công An - Bắc Hà Tower',
        'Hope Residence', 'Oriental Westlake', 'PentStudio',
        'Khu nhà ở 183 Hoàng Văn Thái', 'Vimeco II - Nguyễn Chánh',
        'CT4 Vimeco II', 'GoldSilk Complex', 'Tây Hồ River View',
        'Toà nhà 93 Lò Đúc - Kinh Đô Tower', 'Newhouse Xa La',
        'VP5 Linh Đàm', 'Ngõ 629', 'N02-T1 Ngoại Giao Đoàn', 'Ngõ 151',
        'Vườn Đào', 'Bohemia Residence', 'N01-T8 Ngoại Giao Đoàn',
        'Ecolife Tây Hồ', '101 Láng Hạ', 'KĐT Văn Quán', '107',
        '89 Phùng Hưng', 'Ngô Thì Nhậm', 'Phú Thịnh Green Park', 'Ngõ 77',
        'Khu đô thị Nam Thăng Long - Ciputra', 'Hòa Bình Green Apartment',
        'FLC Garden City', 'Capital Garden 102 Trường Chinh Kinh Đô',
        'Anland Premium', 'Anland LakeView', 'Booyoung',
        'Chung cư Han Jardin', 'Chung cư 536A Minh Khai',
        '282 Nguyễn Huy Tưởng', 'Green Park Tower',
        'Tây Nam Hồ Linh Đàm', 'Thạch Bàn', 'Athena Fulland', 'Dương Nội',
        'Summit Building', 'Hateco Hoàng Mai', 'VP2 Linh Đàm',
        'Tecco Skyville', 'The Golden An Khánh', 'KĐT Vĩnh Hoàng', '61',
        'B4 và B14 Kim Liên', 'Chung cư NO-08 Giang Biên',
        'New Horizon City - 87 Lĩnh Nam', 'HH4 Linh Đàm', 'VOV Mễ Trì',
        'Số 33 ngõ 697 Đường Giải Phóng', 'Gold Tower',
        'Trung tâm thương mại TSQ', 'Rainbow Linh Đàm',
        'N04A Ngoại Giao Đoàn', 'Times Tower - HACC1 Complex Building',
        'Học Viện Quốc Phòng', 'Ngõ 815',
        'Khu đô thị Trung Hòa - Nhân Chính', '65',
        'Sun Grand City Ancora Residence', 'M5 Nguyễn Chí Thanh', 'K2',
        'Green House', 'HUD3 Nguyễn Đức Cảnh', 'Tân Hồng Hà Complex',
        'Diamond Goldmark City', 'Xuân Phương Residence',
        'VC7 Housing Complex - 136 Hồ Tùng Mậu', 'Sunshine Palace',
        'Thăng Long Garden 250 Minh Khai', 'Intracom Riverside',
        'Geleximco Souther Star', 'The Zen Residence', 'Stellar Garden',
        'Trung Yên I', 'Tabudec Plaza', 'Khu đô thị Kim Hoa',
        'PHC Complex 158 Nguyễn Sơn', 'Xuân Mai Tower - CT2 Tô Hiệu',
        'Ngõ 65', 'Canal Park', 'Khu Nhà ở KD Dịch Vọng',
        'Chung cư 24 Nguyễn Khuyến', 'Central Field Trung Kính',
        'MIPEC Towers', 'C3 Lê Văn Lương (Golden Palace)', 'Đặng Xá 2',
        'N02-T3 Ngoại Giao Đoàn', 'Vinaconex 7 - 34 Cầu Diễn', 'Nam Xa la',
        'Chung cư Ruby City CT3', 'CT3 Cổ Nhuế', 'Amber Riverside',
        'CT2 Viettel Trung Văn', 'Lucky House', 'Golden West',
        'Ha Do Park View', 'The Artemis', 'Starcity Lê Văn Lương',
        'N01 - T7 Ngoại Giao Đoàn', '41 Đường Đông Tác', '279',
        'Riverside Tower 79 Thanh Đàm', 'Chung cư C1 Thành Công',
        'C1 C2 Xuân Đỉnh', 'Lilama 124 Minh Khai', 'Hà Thành Plaza',
        'Packexim', 'Ngõ 67B', 'T&T Tower', 'Chung cư C22 Bộ Công an',
        'The Sun Mễ Trì', 'N03-T5 Ngoại Giao Đoàn', 'CT1 Yên Nghĩa',
        'NOXH Đồng Mô', 'Gamuda Gardens', 'Chung cư Yên Hòa Thăng Long',
        'Masteri Water Front', 'Lancaster Luminaire',
        '6 Đường Lê Thánh Tông', 'HP Landmark Tower', 'Kiến Hưng',
        'Khu chung cư Ngô Thì Nhậm', 'Park View Residence Dương Nội',
        'THT New City', 'D’. El Dorado', 'Licogi 13 Tower',
        'Unimax Twin Tower', 'Hemisco Xa La', 'Ecohome 1', 'Mễ Trì Thượng',
        '30 Phạm Văn Đồng', 'Intracom 2 Cầu Diễn', '44', 'Đại Mỗ',
        'Ngõ 199 Phố Trần Quốc Hoàn', '282 Lĩnh Nam',
        'D11 Sunrise Building', 'Ngõ 103', 'CT5-CT6 Lê Đức Thọ',
        'Ruby City', 'Valencia Garden', 'HUD3 Tower', 'D. El Dorado II',
        'D’. El Dorado II', 'Smile Building', 'KĐT Mễ Trì Hạ',
        'Liễu Giai Tower', 'D’. Le Roi Soleil - Quảng An',
        'Vinhomes Smart City Đại Mỗ', 'X2 Đại Kim', 'SME Hoàng Gia',
        'IEC Residences Tứ Hiệp ', 'Khu nhà ở Bộ tư lệnh Thủ đô Hà Nội',
        '158', 'BRG Park Residence', 'N02-T2 Ngoại Giao Đoàn',
        'FLC Complex 36 Phạm Hùng', 'Nghĩa Đô', 'Tổng cục 5 Bộ Công An',
        'Chung cư IEC Residences Tứ Hiệp ', 'Hòa Phát 70 NDC Tower',
        'Hải Đăng Tower', 'MD Complex Mỹ Đình',
        'N03-T3&T4 Ngoại Giao Đoàn', '8B Nguyễn Chí Thanh',
        'PCC1 Triều Khúc', 'Chung cư 51 Quan Nhân', 'Northern Diamond',
        'NHS Trung Văn', 'N03-T1 Ngoại Giao Đoàn',
        'N01-T3 Ngoại Giao Đoàn', 'CT1 Trung Văn - Vinaconex 3',
        'T&T Capella', 'Chelsea Residences', 'Nhà ở xã hội @Home',
        'Chung cư Hoà Phát', 'Viha Complex', 'KĐT mới Cầu Giấy',
        'Lạc Hồng Westlake', 'Sakura Tower']

    duongpho = ['Huỳnh Văn Nghệ', 'Mễ Trì', 'Tố Hữu', 'Tứ Hiệp', 'Nguyễn Văn Giáp',
        'Dương Văn Bé', 'Lê Trọng Tấn', 'Cầu Giấy', 'Hoàng Mai',
        'Phạm Văn Bạch', 'Đại lộ Thăng Long', 'Liễu Giai', 'Hàm Nghi',
        'Trần Phú', 'Phạm Hùng', 'Ngọc Hồi', 'Hồ Tùng Mậu',
        'Nguyễn Văn Huyên', 'Lạc Long Quân', 'Đình Thôn', 'Tô Hiệu',
        'Nguyễn Tuân', 'Võ Chí Công', 'Vũ Phạm Hàm', 'Trần Duy Hưng',
        'Vũ Tông Phan', 'Hoàng Minh Giám', 'Lê Văn Lương', 'Thái Hà',
        'Cương Kiên', 'Thanh Bình', 'Xuân Diệu', 'Mạc Thái Tổ',
        'Nghiêm Xuân Yêm', 'Huỳnh Thúc Kháng', 'Đức Giang', 'Giải Phóng',
        'Xa La', 'Đại Từ', 'Trần Điền', 'Thiên Hiền', 'Hào Nam',
        'Nguyễn Hoàng', 'Trần Hữu Dực', 'Nguyễn Chí Thanh', 'Linh Đường',
        'Lý Thánh Tông', 'Nguyễn Trãi', 'Tây Sơn', 'Phạm Văn Đồng',
        'Minh Khai', 'Kim Giang', 'Thụy Khuê', 'Nguyễn Xiển', 'Trần Bình',
        'Cửa Bắc', 'Tân Mai', 'Láng Hạ', 'Phùng Hưng', 'Trần Hòa', '5',
        'Khuất Duy Tiến', 'Xuân La', 'Tam Trinh', 'Hoàng Đạo Thúy',
        'Vũ Trọng Phụng', 'Trung Kính', 'Kim Mã', 'Phạm Ngọc Thạch',
        'Phùng Chí Kiên', 'Nam Đồng', 'Lê Quang Đạo', 'Châu Văn Liêm',
        'Hồng Tiến', 'Trần Thủ Độ', 'Khâm Thiên', 'Trích Sài', 'Xuân Đỉnh',
        'Nguyễn Cao Luyện', 'Đê La Thành', 'Nguyễn Văn Cừ', 'Chu Huy Mân',
        'Thành Thái', 'Nguyễn Ngọc Vũ', 'Đông Dư', 'Hoàng Cầu',
        'Nguyễn Chánh', 'Vĩnh Hưng', 'Xuân Thủy', '32', 'Chùa Láng',
        'Nguyễn Huy Tưởng', 'Hồng Mai', 'Núi Trúc', 'Tôn Thất Thuyết',
        'Nhân Mỹ', 'Võ Trung Thành', 'Cầu Bươu', 'Trung Hòa',
        'Trần Đăng Ninh', 'Nguyễn Hoàng Tôn', 'Hội Xá', 'Giáp Nhị',
        'Quang Lai', 'Định Công', 'Đông Các', 'Lò Đúc', 'Lê Đức Thọ',
        'Lưu Hữu Phước', 'Đội Cấn', 'Khương Trung', 'Trương Định',
        'Xã Đàn', 'Thanh Nhàn', 'Đa Tốn', 'Thịnh Quang', 'Ô Chợ Dừa',
        'Nguyễn Lương Bằng', 'Văn Khê', '70', 'Nguyễn Cảnh Dị',
        'Đào Nguyên', 'Hồ Mễ Trì', 'Bằng Liệt', 'Vĩnh Phúc', 'Đoàn Khuê',
        'DX 08', 'Sài Đồng', 'Việt Hưng', 'Ngụy Như Kon Tum', 'Chùa Bộc',
        'Bùi Thiện Ngộ', 'Thép Mới', 'Nguyễn Cơ Thạch', 'Dương Đình Nghệ',
        'Văn Cao', 'Nguyễn Công Trứ', 'Lê Văn Thiêm', 'Trần Nguyên Đán',
        'Linh Đàm', 'Tây Mỗ', 'Trần Cung', 'Hải Âu 3', 'Giảng Võ',
        'Trần Quốc Hoàn', 'Duy Tân', 'Quốc lộ 32', 'Ngô Xuân Quảng',
        'Kim Đồng', 'Tôn Thất Tùng', 'Lê Duẩn', 'Quang Trung', 'Hạ Đình',
        'Yên Phụ', 'Chu Văn An', 'Nguyễn Bồ', 'Hoàng Quốc Việt',
        'Nguyễn Duy Trinh', 'Hoàng Liệt', 'Phan Trọng Tuệ',
        'Nguyễn Đức Cảnh', 'Nam Cao', 'Yên Xá', 'Long Biên',
        'Trần Tử Bình', 'Tân Xuân', 'Bưởi', 'Vũ Lăng', 'Trung Văn',
        'Đại Mỗ', 'Yên Lãng', '21B', 'Hải Âu 1', 'Hải Âu', 'Ngọc Khánh',
        'Hoàng Hoa Thám', 'Bùi Xương Trạch', 'Pháp Vân',
        'Nguyễn Phan Chánh', 'Nguyễn Thanh Bình', 'Ngọc Lâm',
        'Hoàng Văn Thái', 'Cầu Am', 'Yên Phúc', 'Thượng Thụy',
        'Trần Văn Lai', 'Phúc Lợi', 'Trần Thái Tông', 'Trần Quý Kiên',
        'Ngô Thì Nhậm', 'Đặng Dung', 'Trần Quý Cáp', 'Mai Dịch',
        'Trường Chinh', 'Lê Trực', 'Trịnh Đình Cửu', 'Bằng A',
        'Thượng Đình', 'Đỗ Đức Dục', 'Nguyên Hồng', 'Võng Thị', 'Bạch Mai',
        'Đông Tác', 'Nguyễn Tam Trinh', 'Hoàng Công', 'Hàm Long',
        'Mai Chí Thọ', 'Lĩnh Nam', 'Lương Thế Vinh', 'Phan Văn Đáng',
        'Đền Lừ 2', 'Tây Kết', 'Chính Kinh', 'Võ Thị Sáu', 'Lương Yên',
        'Hoàng Đạo Thành', 'Trần Khát Chân', 'Giáp Bát', 'Cát Linh',
        'Hồ Ba Mẫu', 'Nguyễn Thái Học', 'Lê Hồng Phong', 'Gia Quất',
        'Trịnh Văn Bô', 'Nghĩa Tân', 'Hồng Hà', 'Ngô Miễn', 'Thành Công',
        'Nguyễn Sơn', 'An Đào', 'Vạn Bảo', 'Nguyễn Khuyến',
        'Nguyễn Đức Thuận', 'K2', 'Mạc Thị Bưởi', 'Lê Xuân Điệp',
        'Nguyễn Văn Trác', 'Vọng', 'Thái Thịnh', 'Cự Lộc', 'Thanh Đàm',
        'Lý Sơn', 'An Dương Vương', 'Quốc Lộ 5B', 'Láng',
        'Doãn Kế Thiện', 'Hàng Vôi', 'Nguyễn Phong Sắc', 'Nguyễn Khoái',
        'Nguyễn Lam', 'Kẻ Vẽ', '50', 'Vĩnh Hồ', 'Cầu Diễn',
        'Khương Thượng', 'Linh Lang', 'Đỗ Nhuận', 'Nguyễn Khánh Toàn',
        'Thịnh Liệt', 'Vĩnh Tuy', 'Ngọc Đại', 'Ngọc Hà', '70A',
        'Giang Biên', 'Phúc Diễn', 'Lạc Trung', 'Lê Thánh Tông',
        'Đặng Xuân Bảng', 'Vũ Trọng Khánh', 'Phương Mai', 'Mỹ Đình',
        'Âu Cơ', 'Khương Hạ', 'Lương Định Của', 'Cửu Việt',
        'Đại lộ Chu Văn An', 'Đại Cồ Việt', 'Tôn Quang Phiệt', 'Yên Nghĩa',
        'Kim Ngưu', 'Vân Hồ 3', 'Quốc Tử Giám', 'Đoàn Thị Điểm',
        'Kim Liên', 'Triều Khúc', 'Quan Nhân', 'Vành Đai 3.5',
        'Trần Kim Xuyến', 'Hưng Thịnh', '25', 'Mai Động']

    xaphuong = ['Sài Đồng', 'Mễ Trì', 'Nguyễn Du', 'Tứ Hiệp', 'An Khánh',
        'Cầu Diễn', 'Tây Mỗ', 'Đông Ngạc', 'Dương Xá', 'Vĩnh Tuy',
        'La Khê', 'Mỹ Đình 1', 'Dịch Vọng', 'Xuân Tảo', 'Hoàng Văn Thụ',
        'Yên Nghĩa', 'Yên Hòa', 'Ngọc Khánh', 'Mỗ Lao', 'Hoàng Liệt',
        'Phú Diễn', 'Xuân La', 'Phú Thượng', 'Mỹ Đình 2', 'Vân Canh',
        'Hà Cầu', 'Thanh Xuân Trung', 'Trung Hòa', 'Khương Đình',
        'Vĩnh Tuy', 'Nhân Chính', 'Trung Liệt', 'Trung Văn',
        'Trung Liệt', 'Quảng An', 'Văn Quán', 'Đại Kim', 'Láng Thượng',
        'Đức Giang', 'Giáp Bát', 'Phúc La', 'Định Công', 'Dương Nội',
        'Ô Chợ Dừa', 'Láng Thượng', 'Láng Hạ', 'Ngã Tư Sở',
        'Cổ Nhuế 1', 'Tân Triều', 'Điện Biên', 'Tả Thanh Oai',
        'Thụy Khuê', 'Mai Dịch', 'Trúc Bạch', 'Tương Mai', 'Giang Biên',
        'Kiến Hưng', 'Đông Hội', 'Phú Đô', 'Mai Động', 'Đội Cấn',
        'Kim Liên', 'Nghĩa Đô', 'Nam Đồng', 'Bồ Đề', 'Thượng Đình',
        'Khâm Thiên', 'Bưởi', 'Xuân Đỉnh', 'Đại Mỗ', 'Thịnh Quang',
        'Phúc Lợi', 'Khương Trung', 'Đa Tốn', 'Đội Cấn', 'Minh Khai',
        'Phú La', 'Vĩnh Hưng', 'Dịch Vọng Hậu', 'Thanh Xuân Nam',
        'Thanh Nhàn', 'Kim Mã', 'Giảng Võ', 'Tân Mai', 'Phố Huế',
        'Láng Hạ', 'Trâu Quỳ', 'Ngọc Thụy', 'Việt Hưng', 'Thịnh Liệt',
        'Thành Công', 'Vạn Phúc', 'Hàng Bột', 'Phạm Đình Hổ',
        'Giảng Võ', 'Yên Sở', 'Ngọc Hà', 'Đống Mác', 'Thanh Nhàn',
        'Đống Mác', 'Phương Canh', 'Quan Hoa', 'Vĩnh Phúc', 'Đặng Xá',
        'Phương Mai', 'Phố Huế', 'Nghĩa Tân', 'Xuân Phương', 'Tân Lập',
        'Bạch Mai', 'Thạch Hòa', 'Yết Kiêu', 'Trúc Bạch',
        'Thượng Thanh', 'Ngọc Lâm', 'Vĩnh Phúc', 'Thịnh Quang',
        'Phú Lãm', 'Phương Liệt', 'Kim Giang', 'Nhật Tân', 'Cổ Nhuế 2',
        'Liễu Giai', 'Phúc Đồng', 'Quán Thánh', 'Quốc Tử Giám',
        'Thanh Xuân Bắc', 'Thạch Bàn', 'Liễu Giai', 'Bạch Mai',
        'Ô Chợ Dừa', 'Ngọc Hà', 'Hàng Bài', 'Bạch Đằng', 'Bạch Đằng',
        'Quang Trung', 'Cát Linh', 'Phương Liên', 'Điện Biên',
        'Vĩnh Ngọc', 'Trần Phú', 'Chương Dương Độ', 'Kim Hoa',
        'Khương Mai', 'Đồng Tâm', 'Thổ Quan', 'Thanh Trì',
        'Phan Chu Trinh', 'Kim Chung', 'Lý Thái Tổ', 'Khương Thượng',
        'Cống Vị', 'Lĩnh Nam', 'Nguyễn Trãi', 'Thanh Lương', 'Cống Vị',
        'Tràng Tiền', 'Bách Khoa', 'Bách Khoa', 'Quán Thánh',
        'Lê Đại Hành', 'Văn Chương', 'Khương Thượng', 'Long Biên',
        'Trung Tự']

    quanhuyen = ['Long Biên', 'Nam Từ Liêm', 'Hai Bà Trưng', 'Thanh Trì',
        'Hoài Đức', 'Bắc Từ Liêm', 'Gia Lâm', 'Hà Đông', 'Cầu Giấy',
        'Hoàng Mai', 'Ba Đình', 'Tây Hồ', 'Thanh Xuân', 'Đống Đa',
        'Đông Anh', 'Tân Triều', 'Đan Phượng', 'Thạch Thất', 'Hoàn Kiếm',
        'Mê Linh']


    code_duan = [244, 140, 474, 390, 268, 179, 262, 269, 373, 374, 330, 404,  98,
        281, 125, 492, 132, 141, 417, 471, 472, 470,  50, 413, 475, 346,
        144,  20,  88, 396,  30, 270, 180, 135, 453, 331, 293, 343, 259,
        372, 258, 325,  41, 229,  69, 425, 422, 106, 145, 297, 221, 169,
        121, 200, 377,  49, 131, 234, 111, 237, 416, 303, 276, 206, 473,
            62, 226, 411, 138, 160, 153, 238,  97, 503, 199,  28, 251, 369,
        407,  90, 397,  99, 428, 208, 272, 108, 147, 115, 119, 224, 274,
        171, 436, 342, 440, 442, 405, 154, 151, 347, 431, 432, 256, 345,
        484,   4, 360, 452,  46,  44, 114, 479,  89, 423, 412, 500,   2,
        480, 485, 426, 354, 174, 401, 230, 105, 209, 356, 402, 231,  94,
        341, 110, 430,  26, 476, 409, 384, 314,  76, 486, 202, 133,  31,
        477, 198, 439, 139, 192, 309, 188, 241, 358, 225, 265,   7, 294,
        367,  21, 164, 351, 127, 406, 438, 250, 210, 393, 165, 482, 355,
            96, 239, 414,  25, 240,  85, 143, 338, 129,  87, 420, 109, 506,
            45,  29, 176, 371, 167, 392,  24,  91, 236, 193, 435, 403, 340,
            42, 389, 184,  52, 504, 387, 170, 287, 455, 149, 408, 243,  84,
        267, 137, 362, 483, 177,  63, 155, 363, 394, 469, 182, 245,  12,
        448, 166, 481,  71, 376,  37, 100, 317, 146,  60, 329, 378, 445,
        292, 101, 499, 410, 494, 382,  40, 379,  58, 353, 361, 118, 332,
        498, 450, 157, 196, 335, 216, 449, 211, 399, 349, 493,  15, 181,
            36, 357, 275, 253, 459, 336, 461, 117, 266, 400, 183, 264, 380,
        487, 156, 263, 220, 113, 273, 280, 304, 205, 488, 185, 365, 466,
        290,  57,   5, 301, 299, 443, 419, 310, 201, 497, 464, 194, 501,
        126, 321,  38, 123, 175,  34, 227, 222, 124, 195, 319, 152, 260,
        173, 418,  75,   6, 424, 468,  19, 323, 278, 490,  54, 178, 324,
        334, 214, 465,  64, 136, 446, 434, 302, 460, 312, 283, 306, 489,
            47, 282, 116,   0, 232,   1,  22, 307, 337, 316, 218, 187, 122,
            67,  33,  32,  48,  79,  74,  10, 150, 447, 429,  35, 102, 368,
        168, 458, 391, 398, 233,  17,  39,  82, 300, 158, 457, 381, 134,
        441, 339, 291, 433, 191, 318, 219,  18, 370, 254, 207, 148, 161,
        444,  95, 496, 456, 375, 427, 204, 130, 421, 366, 437, 388, 217,
        327, 495, 313,  66, 212,  72,  68, 257,  53, 505, 285, 467, 298,
            83,  61,  27,  59, 249, 142, 163, 395, 364, 277,  13,   8, 344,
            77,  51, 247, 186, 328, 315, 385,  78, 415, 289,  56, 296, 128,
            86, 261, 242,  16, 159, 223, 213, 333, 386, 103, 246, 454, 172,
        112, 271,  11, 203,  14, 502, 311,   9,  93, 308,  65, 348, 462,
        162,  92, 104, 359, 228, 248, 107, 478, 491, 350, 197, 215,   3,
            43, 284, 120, 305, 451,  81, 189, 190, 255, 288,  23, 326,  73,
        322, 295, 286, 279,  55, 383,  70, 320,  80, 463, 235, 252, 352]
    code_duongpho = [ 52, 114, 234, 235, 147,  33,  92,  26,  45, 174, 282,  84,  54,
        213, 172, 157,  64, 148, 106, 274, 230, 145, 239, 250, 207, 253,
            46,  94, 190,  22, 184, 257, 112, 118,  51, 290,  39, 256, 280,
        221, 187,  56, 129, 209, 124,  83, 100, 144, 229, 175, 111,  75,
        197, 150, 205,  27, 225,  87, 168, 208,   3,  70, 258, 183,  50,
        252, 200,  77, 173, 167, 117,  90,  17,  67, 218,  71, 202, 260,
        122, 273, 146,  15, 189, 137, 276,  42, 123, 245, 259,   2,  20,
        131,  66, 163, 232, 162, 241,  24, 199, 222, 130,  68,  38, 177,
        286, 275,  98,  97, 102, 289,  74, 203, 261, 185, 269, 196, 268,
        136, 244,   5, 127, 272,  63,  14, 247, 270,  30, 182, 236, 161,
            19,   9, 192, 126,  34, 243, 125,  95, 212,  82, 228, 206,  61,
            40, 216,  32, 181, 155,  79, 233,  88, 178,  58, 265,  16, 121,
            47, 128,  44, 164, 151, 116, 266,  85, 219, 226,  11, 249, 201,
        279, 262,   0,  60,  59, 158,  43,  10, 166, 138, 142, 159,  48,
            23, 264, 193, 220, 170, 217, 215, 154, 283, 214, 109, 204,  93,
        224,  13, 194, 288, 120, 242,  12, 277, 141,  41,  53, 108, 101,
        103, 165, 285, 227,  18, 240, 104,  49, 210,  37,  21,  62, 143,
            89,  35, 223, 119,  65, 153, 188, 140,   8, 254, 133, 152,  69,
        113,  96, 149, 255, 191,  29, 186,  99,   7, 179,  86,  31,  55,
        139, 132, 135,  80,   4, 246,  25,  73,  81, 287, 134, 195, 248,
        160, 156,   6,  36, 169, 107,  91, 284, 251, 171, 115, 267,  72,
        105,  28, 281, 278, 231, 263,  78, 238, 180, 271,  76, 198, 176,
        237, 211,  57,   1, 110]
    code_xaphuong = [ 94,  55,  65, 128,   0,  12, 125, 154,  17, 138,  41,  57,  18,
        142,  27, 145, 144,  64,  56,  26,  75, 140,  78,  58, 132,  28,
        101, 112,  34, 130,  70, 114, 116, 113,  93, 134, 158,  49, 164,
            22,  80, 161,  16, 148,  43,  42,  60,  14, 124, 151, 127, 111,
            52, 120, 126,  20,  40, 153,  79,  53, 163,  38,  62,  59,   8,
        106,  29,   5, 143, 159, 103,  81,  33, 150, 157,  54,  76, 135,
            19, 100,  96,  39,  21, 123,  74,  48, 119,  69, 131, 109, 102,
        139,  25,  73,  23, 146,  67, 156,  97, 162,  83,  88, 137, 160,
            86,  87,  61, 141, 122,   2, 108, 147, 117, 105,  68, 129, 110,
            77,  85,  36,  71,  15,  44,  82,  90,  92,  99, 107,  45,   6,
        149,  63,  24,   7,   3,  89,   9,  84, 152, 136, 121,  10,  37,
            30, 155, 104,  98,  72,  35,  47,  31,  13,  51,  66,  95,  11,
        118,   1,   4,  91,  50, 133,  32,  46, 115]
    code_quanhuyen = [ 9, 11,  4, 12,  5,  1,  3,  8,  2,  7,  0, 16, 13, 19, 18, 15, 17,
        14,  6, 10]

    quanhuyen_dict = dict(zip(quanhuyen, code_quanhuyen))
    xaphuong_dict = dict(zip(xaphuong, code_xaphuong))
    duongpho_dict = dict(zip(duongpho, code_duongpho))
    duan_dict = dict(zip(duan, code_duan))

    selected_quanhuyen = st.selectbox("Chọn Quận(Huyện):", quanhuyen)
    selected_xaphuong = st.selectbox("Chọn Xã(Phường, Thị Trấn):", xaphuong)
    selected_duongpho = st.selectbox("Chọn Đường(Phố):", duongpho)
    selected_duan = st.selectbox("Chọn Dự án (khu):", duan)

    change_code_quanhuyen = quanhuyen_dict[selected_quanhuyen]
    change_code_xaphuong = xaphuong_dict[selected_xaphuong]
    change_code_duongpho = duongpho_dict[selected_duongpho]
    change_code_duan = duan_dict[selected_duan]

    text_dientich = st.number_input("Diện tích:", value=0, step=1)
    text_sophong = st.number_input("Số phòng:", value=0, step=1)
    text_sotoilet = st.number_input("Số Toilet:", value=0, step=1)
    button = st.button('Gửi')
    if button:
        data = np.array([change_code_duan,change_code_duongpho,change_code_xaphuong,change_code_quanhuyen,text_dientich,text_sophong,text_sotoilet]).reshape(1,-1)
        predict = load.predict(data)
        st.write('Giá dự đoán: '+str(predict))
    pass


if __name__ == '__main__':
    main()