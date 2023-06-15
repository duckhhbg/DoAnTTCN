from django import forms

class DistrictForm(forms.Form):
    duan = ['Le Grand Jardin Sài Đồng', 'Golden Palace', 'Không có',
       'Tecco Garden', 'Moonlight 1 - An Lạc Green Symphony',
       'Hoàng Thành Pearl', 'Masteri West Heights',
       'Moonlight I - An Lạc Green Symphony', 'Sunshine City',
       'Vinhomes Ocean Park Gia Lâm', 'Sunshine Garden', 'Park Kiara',
       'The Manor', 'Discovery Complex', 'N01-T7 Ngoại Giao Đoàn',
       'Feliz Homes', 'Xuân Mai Complex', 'Gemek Premium',
       'Golden Park Tower', 'The Tonkin - Vinhomes Smart City',
       'Vinhomes Green Bay Mễ Trì', 'Vinhomes Metropolis - Liễu Giai',
       'Vinhomes Gardenia', 'Bắc Hà Fodacon',
       'The Sakura - Vinhomes Smart City', 'Vinhomes Skylake',
       'Rose Town', 'Goldmark City', '6th Element', 'Ciputra Hà Nội',
       'The Emerald', 'An Lạc Green Symphony', 'Mulberry Lane',
       'Hyundai Hillstate', 'GoldSeason', 'Udic Westlake',
       'Park View City', 'N05 Trần Duy Hưng', 'Riverside Garden',
       'Mandarin Garden', 'Sunshine Center', 'Mailand Hanoi City',
       'Osaka Complex', 'BRG Diamond Residence',
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
    duongpho = ['Huỳnh Văn Nghệ', 'Mễ Trì', 'Không có', 'Tứ Hiệp',
       'Nguyễn Văn Giáp', 'Dương Văn Bé', 'Lê Trọng Tấn', 'Cầu Giấy',
       'Hoàng Mai', 'Tố Hữu', 'Phạm Văn Bạch', 'Đại lộ Thăng Long',
       'Liễu Giai', 'Hàm Nghi', 'Trần Phú', 'Phạm Hùng', 'Ngọc Hồi',
       'Hồ Tùng Mậu', 'Nguyễn Văn Huyên', 'Lạc Long Quân', 'Đình Thôn',
       'Tô Hiệu', 'Nguyễn Tuân', 'Võ Chí Công', 'Vũ Phạm Hàm',
       'Trần Duy Hưng', 'Vũ Tông Phan', 'Hoàng Minh Giám', 'Lê Văn Lương',
       'Thái Hà', 'Cương Kiên', 'Thanh Bình', 'Xuân Diệu', 'Mạc Thái Tổ',
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
       'Vĩnh Tuy', 'Không có', 'Nhân Chính', 'Trung Liệt', 'Trung Văn',
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

    code_duan = [245, 140, 221, 391, 269, 179, 263, 270, 374, 475, 375, 331, 405,
        98, 282, 125, 493, 132, 141, 418, 472, 473, 471,  50, 414, 476,
       347, 144,  20,  88, 397,  30, 271, 180, 135, 454, 332, 294, 344,
       260, 373, 259, 326,  41, 230,  69, 426, 423, 106, 145, 298, 222,
       169, 121, 200, 378,  49, 131, 235, 111, 238, 417, 304, 277, 206,
       474,  62, 227, 412, 138, 160, 153, 239,  97, 504, 199,  28, 252,
       370, 408,  90, 398,  99, 429, 208, 273, 108, 147, 115, 119, 225,
       275, 171, 437, 343, 441, 443, 406, 154, 151, 348, 432, 433, 257,
       346, 485,   4, 361, 453,  46,  44, 114, 480,  89, 424, 413, 501,
         2, 481, 486, 427, 355, 174, 402, 231, 105, 209, 357, 403, 232,
        94, 342, 110, 431,  26, 477, 410, 385, 315,  76, 487, 202, 133,
        31, 478, 198, 440, 139, 192, 310, 188, 242, 359, 226, 266,   7,
       295, 368,  21, 164, 352, 127, 407, 439, 251, 210, 394, 165, 483,
       356,  96, 240, 415,  25, 241,  85, 143, 339, 129,  87, 421, 109,
       507,  45,  29, 176, 372, 167, 393,  24,  91, 237, 193, 436, 404,
       341,  42, 390, 184,  52, 505, 388, 170, 288, 456, 149, 409, 244,
        84, 268, 137, 363, 484, 177,  63, 155, 364, 395, 470, 182, 246,
        12, 449, 166, 482,  71, 377,  37, 100, 318, 146,  60, 330, 379,
       446, 293, 101, 500, 411, 495, 383,  40, 380,  58, 354, 362, 118,
       333, 499, 451, 157, 196, 336, 216, 450, 211, 400, 350, 494,  15,
       181,  36, 358, 276, 254, 460, 337, 462, 117, 267, 401, 183, 265,
       381, 488, 156, 264, 220, 113, 274, 281, 305, 205, 489, 185, 366,
       467, 291,  57,   5, 302, 300, 444, 420, 311, 201, 498, 465, 194,
       502, 126, 322,  38, 123, 175,  34, 228, 223, 124, 195, 320, 152,
       261, 173, 419,  75,   6, 425, 469,  19, 324, 279, 491,  54, 178,
       325, 335, 214, 466,  64, 136, 447, 435, 303, 461, 313, 284, 307,
       490,  47, 283, 116,   0, 233,   1,  22, 308, 338, 317, 218, 187,
       122,  67,  33,  32,  48,  79,  74,  10, 150, 448, 430,  35, 102,
       369, 168, 459, 392, 399, 234,  17,  39,  82, 301, 158, 458, 382,
       134, 442, 340, 292, 434, 191, 319, 219,  18, 371, 255, 207, 148,
       161, 445,  95, 497, 457, 376, 428, 204, 130, 422, 367, 438, 389,
       217, 328, 496, 314,  66, 212,  72,  68, 258,  53, 506, 286, 468,
       299,  83,  61,  27,  59, 250, 142, 163, 396, 365, 278,  13,   8,
       345,  77,  51, 248, 186, 329, 316, 386,  78, 416, 290,  56, 297,
       128,  86, 262, 243,  16, 159, 224, 213, 334, 387, 103, 247, 455,
       172, 112, 272,  11, 203,  14, 503, 312,   9,  93, 309,  65, 349,
       463, 162,  92, 104, 360, 229, 249, 107, 479, 492, 351, 197, 215,
         3,  43, 285, 120, 306, 452,  81, 189, 190, 256, 289,  23, 327,
        73, 323, 296, 287, 280,  55, 384,  70, 321,  80, 464, 236, 253,
       353]
    code_duongpho = [ 52, 115,  72, 236, 148,  33,  93,  26,  45, 235, 175, 283,  85,
        54, 214, 173, 158,  64, 149, 107, 275, 231, 146, 240, 251, 208,
       254,  46,  95, 191,  22, 185, 258, 113, 119,  51, 291,  39, 257,
       281, 222, 188,  56, 130, 210, 125,  84, 101, 145, 230, 176, 112,
        76, 198, 151, 206,  27, 226,  88, 169, 209,   3,  70, 259, 184,
        50, 253, 201,  78, 174, 168, 118,  91,  17,  67, 219,  71, 203,
       261, 123, 274, 147,  15, 190, 138, 277,  42, 124, 246, 260,   2,
        20, 132,  66, 164, 233, 163, 242,  24, 200, 223, 131,  68,  38,
       178, 287, 276,  99,  98, 103, 290,  75, 204, 262, 186, 270, 197,
       269, 137, 245,   5, 128, 273,  63,  14, 248, 271,  30, 183, 237,
       162,  19,   9, 193, 127,  34, 244, 126,  96, 213,  83, 229, 207,
        61,  40, 217,  32, 182, 156,  80, 234,  89, 179,  58, 266,  16,
       122,  47, 129,  44, 165, 152, 117, 267,  86, 220, 227,  11, 250,
       202, 280, 263,   0,  60,  59, 159,  43,  10, 167, 139, 143, 160,
        48,  23, 265, 194, 221, 171, 218, 216, 155, 284, 215, 110, 205,
        94, 225,  13, 195, 289, 121, 243,  12, 278, 142,  41,  53, 109,
       102, 104, 166, 286, 228,  18, 241, 105,  49, 211,  37,  21,  62,
       144,  90,  35, 224, 120,  65, 154, 189, 141,   8, 255, 134, 153,
        69, 114,  97, 150, 256, 192,  29, 187, 100,   7, 180,  87,  31,
        55, 140, 133, 136,  81,   4, 247,  25,  74,  82, 288, 135, 196,
       249, 161, 157,   6,  36, 170, 108,  92, 285, 252, 172, 116, 268,
        73, 106,  28, 282, 279, 232, 264,  79, 239, 181, 272,  77, 199,
       177, 238, 212,  57,   1, 111]
    code_xaphuong = [ 95,  56,  66, 129,   0,  12, 126, 155,  17, 139,  42,  58,  18,
       143,  27, 146, 145,  65,  57,  26,  76, 141,  79,  59, 133,  28,
       102, 113,  35, 131,  30,  71, 115, 117, 114,  94, 135, 159,  50,
       165,  22,  81, 162,  16, 149,  44,  43,  61,  14, 125, 152, 128,
       112,  53, 121, 127,  20,  41, 154,  80,  54, 164,  39,  63,  60,
         8, 107,  29,   5, 144, 160, 104,  82,  34, 151, 158,  55,  77,
       136,  19, 101,  97,  40,  21, 124,  75,  49, 120,  70, 132, 110,
       103, 140,  25,  74,  23, 147,  68, 157,  98, 163,  84,  89, 138,
       161,  87,  88,  62, 142, 123,   2, 109, 148, 118, 106,  69, 130,
       111,  78,  86,  37,  72,  15,  45,  83,  91,  93, 100, 108,  46,
         6, 150,  64,  24,   7,   3,  90,   9,  85, 153, 137, 122,  10,
        38,  31, 156, 105,  99,  73,  36,  48,  32,  13,  52,  67,  96,
        11, 119,   1,   4,  92,  51, 134,  33,  47, 116]
    code_quanhuyen = [ 9, 11,  4, 12,  5,  1,  3,  8,  2,  7,  0, 16, 13, 19, 18, 15, 17,
       14,  6, 10]
    
    
    quanhuyen_dict = zip(code_quanhuyen, quanhuyen)
    xaphuong_dict = zip(code_xaphuong, xaphuong)
    duongpho_dict = zip(code_duongpho, duongpho)
    duan_dict = zip(code_duan, duan)
    district_quanhuyen = forms.ChoiceField(choices=quanhuyen_dict)
    district_xaphuong = forms.ChoiceField(choices=xaphuong_dict)
    district_duongpho = forms.ChoiceField(choices=duongpho_dict)
    district_duan = forms.ChoiceField(choices=duan_dict)
    district_dientich = forms.IntegerField()
    district_phongngu = forms.IntegerField()
    district_toilet = forms.IntegerField()

# class DistrictForm(forms.Form):
#     code_quanhuyen = [9, 11, 4, 12, 5, 1, 3, 8, 2, 7, 0, 16, 13, 19, 18, 15, 17, 14, 6, 10]
#     quanhuyen = ['Long Biên', 'Nam Từ Liêm', 'Hai Bà Trưng', 'Thanh Trì', 'Hoài Đức', 'Bắc Từ Liêm', 'Gia Lâm', 'Hà Đông', 'Cầu Giấy', 'Hoàng Mai', 'Ba Đình', 'Tây Hồ', 'Thanh Xuân', 'Đống Đa', 'Đông Anh', 'Tân Triều', 'Đan Phượng', 'Thạch Thất', 'Hoàn Kiếm', 'Mê Linh']
    
#     district_choices = zip(code_quanhuyen, quanhuyen)
#     district = forms.ChoiceField(choices=district_choices)