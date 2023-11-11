from adminEmployee import AdminEmp
from working import Working
from sales_repre import Sales


s = [
    AdminEmp("Валерий Задорожный"),
    Working("Илья Кромин", 150),
    Sales("Николай Хорольский", 50)
]
r = 0
print("=" * 30)
print("Расчет заработной платы")
for i in s:
    r += 1
    print(f"Заработная плата: {r} - {i.print_name()}\n- Проверить сумму: {i.zp_all()}")


