class movieTheater(object):
    def __init__(self, name, time, money):
        self.name = name
        self.time = time
        self.money = money


    def showTime(self):
        print(self.time)

    def earnMoney(self, newMoney):
        self.money = self.money + newMoney


class Seat(object):
    def __init__(self, seat):
        self.seat = seat

    def showSeat(self):
        print("X는 예매가 완료된 좌석입니다.")
        for i in range(5):
            for j in range(5):
                if self.seat[i][j] == 0:
                    if i == 0:
                        print('A'+ str(j+1) + ' ', end='')
                    if i == 1:
                        print('B'+ str(j+1) + ' ', end='')
                    if i == 2:
                        print('C'+ str(j+1) + ' ', end='')
                    if i == 3:
                        print('D'+ str(j+1) + ' ', end='')
                    if i == 4:
                        print('E'+ str(j+1) + ' ', end='')
                elif self.seat[i][j] == 1:
                    print("X  ", end='')
            print("\n")


    def reserveSeat(self):
        flag = 1
        for i in range(5):
            for j in range(5):
                flag = self.seat[i][j]*flag
        if flag == 1:
            print("모든 좌석이 예매되었습니다.")
            return 0
        n = int(input("예약할 표의 수를 입력하세요\n"))
        if n<0 or n>25 :
            print("음수와 25보다 큰 수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        junior = int(input("어린이는 몇명입니까?\n"))
        if junior < 0 or junior > n:
            print("인원이 맞지 않습니다. 음수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        senior = int(input("청소년은 몇명입니까?\n"))
        if senior < 0 or senior > n:
            print("인원이 맞지 않습니다. 음수는 입력하지 마세요. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        adult = n - junior - senior
        if adult < 0 :
            print("인원이 맞지 않습니다. 다시 예매를 진행하세요.")
            money = self.reserveSeat()
            return money
        else:
            for k in range(n):
                i = int(input("예약할 좌석의 열(1, 2, 3, 4, 5)를 입력하세요. 1열은 A를 의미합니다.\n"))
                j = int(input("예약할 좌석의 행(1, 2, 3, 4, 5)을 입력하세요\n"))
                if self.seat[i-1][j-1] == 1:
                    print("이미 예매된 좌석입니다. 다시 예매를 진행하세요.")
                    money = self.reserveSeat()
                    return money
                else:
                    self.seat[i-1][j-1] = 1
        print("예매가 완료되었습니다.")
        money = junior*5000 + senior*8000 + adult*10000
        return money


def main():
    TRUE = 1
    FALSE = 0
    BOOL = TRUE
    benefit = 0

    while BOOL:
        print("1. 영화 예매")
        print("2. 영화 시간표 확인")
        print("3. 영화 좌석 확인")
        print("4. 총 수입 보기")
        print("5. 시스템 종료")
        choiceMenu = input("실행할 것을 선택하세요\n")

        if choiceMenu == '1':
            print("1. "+movie1.name)
            print("2. "+movie2.name)
            print("3. "+movie3.name)
            choiceMovie = input("몇 번째 영화를 보시겠습니까\n")

            if choiceMovie == '1':
                movie1.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요\n")
                if choiceTime == '1':
                    movie1_time1.showSeat()
                    benefit = movie1_time1.reserveSeat()
                    movie1.earnMoney(benefit)
                elif choiceTime == '2':
                    movie1_time2.showSeat()
                    benefit = movie1_time2.reserveSeat()
                    movie1.earnMoney(benefit)
                elif choiceTime == '3':
                    movie1_time3.showSeat()
                    benefit = movie1_time3.reserveSeat()
                    movie1.earnMoney(benefit)
                elif choiceTime == '4':
                    movie1_time4.showSeat()
                    benefit = movie1_time4.reserveSeat()
                    movie1.earnMoney(benefit)
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 4사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")

            elif choiceMovie == '2':
                movie2.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요\n")
                if choiceTime == '1':
                    movie2_time1.showSeat()
                    benefit = movie2_time1.reserveSeat()
                    movie2.earnMoney(benefit)
                elif choiceTime == '2':
                    movie2_time2.showSeat()
                    benefit = movie2_time2.reserveSeat()
                    movie2.earnMoney(benefit)
                elif choiceTime == '3':
                    movie2_time3.showSeat()
                    benefit = movie2_time3.reserveSeat()
                    movie2.earnMoney(benefit)
                elif choiceTime == '4':
                    movie2_time4.showSeat()
                    benefit = movie2_time4.reserveSeat()
                    movie2.earnMoney(benefit)
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 4사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")

            elif choiceMovie == '3':
                movie3.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요\n")
                if choiceTime == '1':
                    movie3_time1.showSeat()
                    benefit = movie3_time1.reserveSeat()
                    movie3.earnMoney(benefit)
                elif choiceTime == '2':
                    movie3_time2.showSeat()
                    benefit = movie3_time2.reserveSeat()
                    movie3.earnMoney(benefit)
                elif choiceTime == '3':
                    movie3_time3.showSeat()
                    benefit = movie3_time3.reserveSeat()
                    movie3.earnMoney(benefit)
                elif choiceTime == '4':
                    movie3_time4.showSeat()
                    benefit = movie3_time4.reserveSeat()
                    movie3.earnMoney(benefit)
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 3사이의 시간을 입력해주세요. 프로그램을 다시 시작합니다.")

            else:
                print("없는 영화입니다. 1에서 3사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

        elif choiceMenu == '2':
            choiceMovie = input("어느 영화의 상영시간표를 보시겠습니까? Inception(1), Harry Porter(2), Dunkirk(3)")
            BOOL2 = TRUE
            while BOOL2:
                if choiceMovie == '1':
                    movie1.showTime()
                elif choiceMovie == '2':
                    movie2.showTime()
                elif choiceMovie == '3':
                    movie3.showTime()
                else:
                    print("없는 영화입니다. 1에서 3사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

                choice = input("다른 영화의 상영 시간표를 보시려면 1, 시간표 확인 기능을 종료하시려면 2를 누르세요")
                if choice == '1' :
                    choiceMovie = input("어느 영화의 상영시간표를 보시겠습니까? Inception(1), Harry Porter(2), Dunkirk(3)")
                elif choice == '2':
                    BOOL2 = FALSE
                else:
                    print("1과 2만 입력하세요. 프로그램을 다시 시작합니다.")

        elif choiceMenu == '3':
            print("1. "+movie1.name)
            print("2. "+movie2.name)
            print("3. "+movie3.name)
            choiceMovie = input("몇 번째 영화의 좌석을 보시겠습니까?\n")

            if choiceMovie == '1':
                movie1.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요.\n")
                if choiceTime == '1':
                    movie1_time1.showSeat()
                elif choiceTime == '2':
                    movie1_time2.showSeat()
                elif choiceTime == '3':
                    movie1_time3.showSeat()
                elif choiceTime == '4':
                    movie1_time4.showSeat()
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 4사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

            elif choiceMovie == '2':
                movie2.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요\n")
                if choiceTime == '1':
                    movie2_time1.showSeat()
                elif choiceTime == '2':
                    movie2_time2.showSeat()
                elif choiceTime == '3':
                    movie2_time3.showSeat()
                elif choiceTime == '4':
                    movie2_time4.showSeat()
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 4사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

            elif choiceMovie == '3':
                movie3.showTime()
                choiceTime = input("영화의 상영 순서를 선택해주세요\n")
                if choiceTime == '1':
                    movie3_time1.showSeat()
                elif choiceTime == '2':
                    movie3_time2.showSeat()
                elif choiceTime == '3':
                    movie3_time3.showSeat()
                elif choiceTime == '4':
                    movie3_time4.showSeat()
                else:
                    print("해당 시간은 존재하지 않습니다. 1에서 3사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

            else:
                print("해당 영화는 존재하지 않습니다. 1에서 3사이의 정수를 입력해주세요. 프로그램을 다시 시작합니다.")

        elif choiceMenu == '4':
            allBenefit = movie1.money+movie2.money+movie3.money
            print("총 수입: ")
            print(allBenefit)

        elif choiceMenu == '5':
            print("시스템을 종료합니다")
            BOOL = FALSE

        else:
            print("1에서 5까지의 정수만 입력해주세요")


if __name__ == '__main__':
    movie1 = movieTheater("Inception",'9:00     12:00     15:00     18:00', 0)
    movie1_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie1_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie1_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie1_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    movie2 = movieTheater("Harry Porter", '10:15     13:30     16:45     20:00', 0)
    movie2_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie2_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie2_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie2_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    movie3 = movieTheater("Dunkirk", '10:00     11:40     15:00     22:00', 0)
    movie3_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie3_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie3_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    movie3_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    main()