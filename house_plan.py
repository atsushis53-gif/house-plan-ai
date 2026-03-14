class FloorPlanGenerator:
    def __init__(self, constraints):
        # 1. 前提条件（constraints）を読み込む
        self.constraints = constraints
        self.floor1 = {}
        self.floor2 = {}

    def generate(self):
        # 2. 一番最初に「階段」を配置する（上下階の座標を一致させる）
        # 例として、X:2, Y:2の位置に、幅1・奥行き2の階段を固定する
        stairs_position = {"x": 2, "y": 2, "width": 1, "height": 2}
        self.floor1["Stairs"] = stairs_position
        self.floor2["Stairs"] = stairs_position

        # 3. 前提条件に基づいて、残りの部屋を配置していく
        self._place_rooms()

        return {"1F": self.floor1, "2F": self.floor2}

    def _place_rooms(self):
        # ここに、LDKや寝室をパズルのように配置していくロジックを書く
        # 前提条件（self.constraints）を参照しながらサイズなどを決める
        target_ldk_size = self.constraints.get("min_ldk_size", 15)
        # ...配置処理...
        pass

# ==========================================
# 実行部分（前提条件の入れ方）
# ==========================================

# クライアントの要望（前提条件）を辞書形式で定義する
client_requirements = {
    "total_area_sqm": 100,      # 建坪（平米）
    "family_size": 4,           # 家族構成
    "min_ldk_size": 18,         # LDKは18帖以上
    "has_car": True,            # 駐車場が必要か
    "direction": "south"        # 南向き
}

# 条件を渡して、AIに間取りを生成させる
ai_generator = FloorPlanGenerator(constraints=client_requirements)
result = ai_generator.generate()

print("生成された間取りデータ:", result)
