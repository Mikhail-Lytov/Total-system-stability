#from Error_Len_Object_C import Error_Len_Object_C

hour_operation = [[1,2],[5,6],[1,10]]#средняя стоимость часа функционирования
T_work = [[2,1],[7,9],[10,2]]#Т_Рем
B = [[3,4],[3,2],[3,2]]
number_repair_tools = [[2,1],[7,9],[10,2]] # Ncp
cost_repair_tools = [[1,2],[5,6],[1,10]] # Cpr
number_repairmen = [[2,1],[7,9],[10,2]] # NРП
cost_repairmen = [[1,2],[5,6],[1,10]] # Cрп
number_repair_and_evacuation_facilities = [[[1,2],[1,3]],[[1,4],[1,5]],[[1,6],[1,7]]] #Фuh
cost_and_evacuation_facilities = [[[1,2],[1,3]],[[1,4],[1,5]],[[1,6],[1,7]]] # Cфиh
# add 2.5.3 + B
def add_hour_operation(operation):## самому писать какой элемент ввести
    global hour_operation
    hour_operation.append(operation)

def add_T_work(operation):
    global T_work
    T_work.append(operation)

def B_RP(operation):
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

def cost_of_formation(): # проверить
    result = 0.0
    for i in range(len(number_repair_tools)):
        for j in range(2):
            result += number_repair_tools[i][j] * cost_repair_tools[i][j] + number_repairmen[i][j] * cost_repairmen[i][j]
            for k in range(len(number_repair_and_evacuation_facilities[i][j])):
                result += number_repair_and_evacuation_facilities[i][j][k] * cost_and_evacuation_facilities[i][j][k]
            result *= B[i][j]
    print(result)

def cost_performance():
    result = 0.0
    if(len(hour_operation) == len(B) and len(hour_operation) == len(T_work)):
        for i in range(len(hour_operation)):
            for j in range(2):
                result += B[i][j] * T_work[i][j] * hour_operation[i][j]
        return result

    else: print('пиздец')


def cost_transportation():
    pass

def calculation(): #стоимость формирования

    cost_of_formation()#
    performance = cost_performance()# стоимость выполнения
    cost_transportation()#стоимость транспортировки


if __name__ == '__main__':
    calculation()
# переделать окно, теперь пользователь может только
# вписывать данный, а мы решаем все остальное