# 초기 과일 재고 설정
inventory = {
    "사과": 3,
    "바나나": 3,
    "오렌지": 3,
    "포도": 3,
    "수박": 3
}

def display_inventory():
    """현재 재고를 출력하는 함수"""
    print("\n현재 재고:")
    for fruit, count in inventory.items():
        print(f"{fruit}: {count}개")

def is_store_empty():
    """재고가 모두 소진되었는지 확인하는 함수"""
    return all(count == 0 for count in inventory.values())

print(inventory)
print("과일 가게에 오신 것을 환영합니다!\n")

# 메인 루프
while True:
    # 현재 재고 표시
    display_inventory()

    # 구매할 과일 입력 받기
    choice = input("구매할 과일을 입력하세요 (종료하려면 '종료' 입력): ").strip()

    if choice == "종료":
        print("가게를 종료합니다. 방문해 주셔서 감사합니다!")
        break

    if choice not in inventory:
        print("해당 과일은 판매하지 않습니다. 다시 선택해주세요.")
        continue

    if inventory[choice] > 0:
        inventory[choice] -= 1
        print(f"{choice}를 구매하셨습니다!")
    else:
        print(f"{choice}는 품절입니다. 다른 과일을 선택해주세요.")

    # 재고가 모두 소진되었는지 확인
    if is_store_empty():
        print("\n모든 과일이 판매되었습니다. 가게를 종료합니다!")
        break
