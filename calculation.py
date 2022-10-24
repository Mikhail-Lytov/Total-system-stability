#from Error_Len_Object_C import Error_Len_Object_C

hour_operation = [[1,2],[5,6],[1,10]]#средняя стоимость часа функционирования
T_work = [[2,1],[7,9],[10,2]]#Т_Рем
B = [[3,4],[3,2],[3,2]]
def add_hour_operation(operation):## самому писать какой элемент ввести
    global hour_operation
    hour_operation.append(operation)

def add_T_work(operation):
    global T_work
    T_work.append(operation)

def B_RP(operation):
    global B
    B.append(operation)

def cost_of_formation():
    pass

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
