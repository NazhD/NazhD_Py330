from adminEmployee import AdminEmp
from working import Working
from sales_repre import Sales


s = [
    AdminEmp("Viktor"),
    Working("Vika", 150),
    Sales("Vika", 50)
]
r = 0
for i in s:
    r += 1
    print(f"Заработная плата: {r} - {i.print_name()}\n- Проверить сумму: {i.zp_all()}")


