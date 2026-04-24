import pandas as pd
from geopy.geocoders import Nominatim
import time

# CSVファイルを読み込む
df = pd.read_csv('(csv)★10-2在日米軍施設・区域の状況 (専用施設)別一覧.csv')

# ジオコーダーを初期化
geolocator = Nominatim(user_agent="us_bases_geocoder")

# 緯度と経度の列を追加
df['latitude'] = None
df['longitude'] = None

# 各行の所在地1をジオコーディング
for index, row in df.iterrows():
    location_str = row['所在地1']
    if pd.notna(location_str) and location_str != '-':
        try:
            location = geolocator.geocode(location_str + ', Japan')
            if location:
                df.at[index, 'latitude'] = location.latitude
                df.at[index, 'longitude'] = location.longitude
            else:
                print(f"Location not found for: {location_str}")
        except Exception as e:
            print(f"Error geocoding {location_str}: {e}")
        time.sleep(1)  # APIのレート制限を避けるため

# 結果を新しいCSVに保存
df.to_csv('us_bases_with_coords.csv', index=False, encoding='utf-8')

print("Geocoding completed. Output saved to us_bases_with_coords.csv")