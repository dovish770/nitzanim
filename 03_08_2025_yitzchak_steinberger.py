# ********** Q1 **********
def q1(num):
    string_to_print = f"{num} " #המחזורת שתכיל לבסוף את רשימת כל המספרים שהגענו אליהם

    #תנאי עצירה - תמשיך עד שנגיע לתוצאה 1
    #אם המספר אי זוגי - הכפל ב3 והוסף 1
    #אם המספר זוגי - חלק ב2
    #אחרי כל פעולה תוסיף למחרוזת המכילה את כל התוצאות בדרך
    while num > 1: 
        if num % 2: 
            num = num * 3 + 1 
        else: 
            num = num // 2
        string_to_print += f"-> {num} "

    print(string_to_print + "Done")
    pass

"""
Helper functions for question 1 will be written here.
"""

# ********** Q2 **********
def q2():
    array_of_arrays = create_arrays() #פונקציה שיוצרת את המטריצה
    rotated_arrays = rotate_arrays(array_of_arrays) #פונקציה שמסובבת את המטריצה
    switched_arrays = switch_arrays(rotated_arrays) #פונקציה שעוד פעם מחליפה את המקומות שלהם

    sum_culmn_8 = 0
    arr_with_89 = -1
    heighest_devided_by_7 = -1

    for index, arr in enumerate(switched_arrays):
        sum_culmn_8 += arr[8]

        if 89 in arr:
            arr_with_89 = index
        
        if index == 7:
            for num in arr:
                if num % 7 == 0:
                   if heighest_devided_by_7 < num :
                         heighest_devided_by_7 = num

        print(arr)

    print(f"Q2A={sum_culmn_8}")
    print(f"Q2B={arr_with_89}")
    print(f"Q2C={heighest_devided_by_7}")
    
    
    pass

"""
Helper functions for question 2 will be written here.
"""
def create_arrays():
    """
    פונקציה שיוצרת מטריצה דו מימדית של 12*12 תאים, עם מספרים מסודרים מ1-144
    """
    array_of_arrays = []
    counter = 1
    for i in range (12): #בכל איטרציה נוצרת רשימה חדשה
        cur_arr = []
        for j in range(12): #בכל איטרציה  מתווסף לרשימה מספר חדש הבא ברשימה
            cur_arr.append(counter)
            counter += 1
        array_of_arrays.append(cur_arr)    
    return array_of_arrays

def rotate_arrays(arr):
    """
    מקבלת מטריצה דו מימדית, ועל כל זוג שורות מבצעת פעולה, ומחזירה אותה מוכנה
    """
    for i in range(0, 12, 2):  # בכל איטרציה מטפלים בזוג שורות
        cur_arrs = handle_2_arrays(arr[i], arr[i+1])  # מפעילים את פונקציית העיבוד על הזוג
        arr[i] = cur_arrs[0]     # מחליפים את השורה הראשונה בתוצאה
        arr[i+1] = cur_arrs[1]   # ואת השנייה בתוצאה השנייה
    return arr


def handle_2_arrays(arr1, arr2):
    """
    מקבלת שני מערכים 
    מבצעת עליהם סדרת פעולות
    ומחזירה את המערכים לאחר העיבוד
    """
    for i in range(0, 12, 2):  # עובר על האינדקסים 0, 2, 4, 6, 8, 10
        if i in (0, 4, 8): # כלומר - כל זוג שני - החל מהראשון - ינוע עם כיוון השעון
            arr1, arr2 = with_clock(arr1, arr2, i)
        else: #כל זוג שני - החל מהשני - ינוע נגד כיוון השעון
            arr1, arr2 = reverse_clock(arr1, arr2, i)
    return [arr1, arr2]


def with_clock(arr1, arr2, i):
    """
    מבצעת החלפה של ארבעה איברים בשתי שורות לפי אינדקס נתון, עם כיוון השעון
    מחזירה את השורות לאחר השינוי.
    """
    cur_num = arr1[i+1]
    arr1[i+1] = arr1[i]
    arr1[i] = arr2[i]
    arr2[i] = arr2[i+1]
    arr2[i+1] = cur_num

    return arr1, arr2


def reverse_clock(arr1, arr2, i):
    """
    מבצעת החלפה של ארבעה איברים בשתי שורות לפי אינדקס נתון, נגד כיוון השעון
    מחזירה את השורות לאחר השינוי.
    """
    cur_num = arr1[i]
    arr1 [i] = arr1[i+1]
    arr1[i+1] = arr2[i+1]
    arr2[i+1] = arr2[i]
    arr2[i] = cur_num
    return arr1,arr2

def switch_arrays(arr_of_arrays):
    """
    מחלקת תת-מטריצות בגודל 2 על 2 בתוך מטריצה דו-ממדית בגודל 12 על 12
    ואז מחליפה כל האחד עם מי שכנגדו באלכסון ממנו
    """
    for i in range(0, 12, 2):  
        for j in range(0, 12, 4): 

            arr1 = [
                [arr_of_arrays[i][j], arr_of_arrays[i][j+1]],
                [arr_of_arrays[i+1][j], arr_of_arrays[i+1][j+1]]
            ]

            arr2 = [
                [arr_of_arrays[i][j+2], arr_of_arrays[i][j+3]],
                [arr_of_arrays[i+1][j+2], arr_of_arrays[i+1][j+3]]
            ]

            arr_of_arrays[i][j], arr_of_arrays[i][j+1]     = arr2[0][0], arr2[0][1]
            arr_of_arrays[i+1][j], arr_of_arrays[i+1][j+1] = arr2[1][0], arr2[1][1]

            arr_of_arrays[i][j+2], arr_of_arrays[i][j+3]     = arr1[0][0], arr1[0][1]
            arr_of_arrays[i+1][j+2], arr_of_arrays[i+1][j+3] = arr1[1][0], arr1[1][1]

    return arr_of_arrays


# ********** Q3 **********
"""
The class for question 3 will be written here.
"""
class Item:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def set_name(self, name: str):
        self._name = name

    def set_price(self, price: float):
        if price < 0:                        #מוודא שלא הוכנס ערך לא חוקי
            raise ValueError("Price cannot be negative")
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price



# ********** Q4 **********
def q4(paintings):
    result = recursive_helper(paintings, 80000, 0, 0, [])
    Q4A = len(result[1])
    Q4B = result[0]
    Q4C = result[2]

    print(f"Q4A = {Q4A}")
    print(f"Q4B = {Q4B}")
    print(f"Q4C = {Q4C}")
    pass




"""
Helper functions for question 4 will be written here.
"""

def recursive_helper(paintings, remainig_budget, people, i, chosen_paintings):
    if i >= len(paintings):
        return people, chosen_paintings, remainig_budget

    taken = (0, [])
    if paintings[i][1] <= remainig_budget:
        copy_chosen = chosen_paintings.copy()
        copy_chosen.append(paintings[i])
        taken = recursive_helper(
            paintings,
            remainig_budget - paintings[i][1],
            people + paintings[i][2],
            i + 1,
            copy_chosen, 
        )

    not_taken = recursive_helper(
        paintings,
        remainig_budget,
        people,
        i + 1,
        chosen_paintings
    )

    if taken[0] > not_taken[0]:
        return taken
    else:
        return not_taken




