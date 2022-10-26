# from Error_Len_Object_C import Error_Len_Object_C

hour_operation = [[1, 2], [5, 6], [1, 10]]  # средняя стоимость часа функционирования
T_work = [[2, 1], [7, 9], [10, 2]]  # Т_Рем
B = [[3, 4], [3, 2], [3, 2]]
number_repair_tools = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]   # Ncp
cost_repair_tools = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]  # Cpr
number_repairmen = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]   # NРП
cost_repairmen = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]  # Cрп
number_repair_and_evacuation_facilities = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]  # Фuh
cost_and_evacuation_facilities = [[[1, 2], [1, 3]], [[1, 4], [1, 5]], [[1, 6], [1, 7]]]  # Cфиh
cost_km_travel = [[7, 8, 9, 0], [1, 2, 3, 4]]  # стоимотсь одного километра перемещния РПМТ
distance_travel = [[1, 2, 3, 4], [3, 4, 5, 6]]  # Расстроянеи между PO уровня, пройденное РПМТ
cost_km_transpot = [[7, 8, 9, 0], [1, 2, 3, 4]]  # стоимоть одного км транспортировки
distance_transportation = [[1, 2, 3, 4], [3, 4, 5, 6]]  # Расстояние между РО
number_samples_funds = [[1, 2, 3, 4], [3, 4, 5, 6]]  # количество образцов средств


# 2.5.4
def cost_travel():
    result = 0.0
    for i in range(len(cost_km_travel)):
        for j in range(len(distance_travel[i])):  # уровень заявки
            result += cost_km_travel[i][j] * distance_travel[i][j]
    return result


def cost_transportation_ATO():
    result = 0.0
    for i in range(len(cost_km_transpot)):
        for j in range(len(cost_km_transpot[i])):
            result += cost_km_transpot[i][j] * distance_transportation[i][j] * number_samples_funds[i][j]
    return result


# 2.5.6
def add_cost_km_transpot(element):
    global cost_km_transpot
    cost_km_transpot.append(element)


def add_distance_transportation(element):
    global distance_transportation
    distance_transportation.append(element)


def add_number_samples_funds(element):
    global number_samples_funds
    number_samples_funds.append(element)


# 2.5.5
def add_distance(element):
    global distance_travel
    distance_travel.append(element)


def add_km_travel(element):
    global cost_km_travel
    cost_km_travel.append(element)


# add 2.5.3 + B
def add_hour_operation(operation):  ## самому писать какой элемент ввести
    global hour_operation
    hour_operation.append(operation)
    print(hour_operation)


def add_T_work(operation):
    global T_work
    T_work.append(operation)


def add_B_RP(operation):
    global B
    B.append(operation)


# add 2.5.2
def add_number_repair_tools(element):
    global number_repair_tools
    number_repair_tools.append(element)


def add_cost_repair_tools(element):
    global cost_repair_tools
    cost_repair_tools.append(element)


def add_number_repairmen(element):
    global number_repairmen
    number_repairmen.append(element)


def add_cost_repairmen(element):
    global cost_repairmen
    cost_repairmen.append(element)


def add_number_repair_and_evacuation_facilities(element):
    global number_repair_and_evacuation_facilities
    number_repair_and_evacuation_facilities.append(element)


def add_cost_repair_and_evacuation_facilities(element):
    global cost_and_evacuation_facilities
    cost_and_evacuation_facilities.append(element)


def cost_of_formation():  # проверить
    result = 0.0
    for i in range(len(number_repair_tools)):
        for j in range(2):
            for t in range(len(number_repair_tools[i][j])):
                result += number_repair_tools[i][j][t] * cost_repair_tools[i][j][t] + number_repairmen[i][j][t] * \
                          cost_repairmen[i][j][t]
            for k in range(len(number_repair_and_evacuation_facilities[i][j])):
                result += number_repair_and_evacuation_facilities[i][j][k] * cost_and_evacuation_facilities[i][j][k]
            result *= B[i][j]
    return result


def cost_performance():
    result = 0.0
    if (len(hour_operation) == len(B) and len(hour_operation) == len(T_work)):
        for i in range(len(hour_operation)):
            for j in range(2):
                result += B[i][j] * T_work[i][j] * hour_operation[i][j]
        return result

    else:
        print('пиздец')


def cost_transportation():
    result = cost_travel() + cost_transportation_ATO()
    return result


def calculation():  # стоимость формирования

    formation = cost_of_formation()  #
    performance = cost_performance()  # стоимость выполнения
    transportation = cost_transportation()  # стоимость транспортировки

    result = formation + performance + transportation

    return result


if __name__ == '__main__':
    calculation()
# переделать окно, теперь пользователь может только
# вписывать данный, а мы решаем все остальное
