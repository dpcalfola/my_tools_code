# 소비 전력량 계산기 (Power Consumption Calculator) v0.1

<br>

> ### Execution file: main.py
>
> ### 실행 파일: main.py

<br><br>

# < Document list >

1. [English manual](#EnglishManual)
2. [한국어 설명서](#KoreanManual)

<br><br><br>

<a name="EnglishManual">

# 1. English Manual

</a>

> ### 1.1. Introduction
>
> This Python code calculates the total power consumption of the user's electronic devices
>
> The code contains three parts: class, data, and main.

> ### 1.2 Documentation of three parts
>
> > #### 1.2.1 Class part:
> >
> > There are two classes defined in this part: Device and Electrics.
> > The Device class takes in the name, power, count, and use_time_a_day of the device as arguments in its constructor
> > method.
> > The Electrics class inherits from the Device class and adds two methods, daily_power and total_power. The
> > daily_power
> > method calculates the daily power consumption of the device, while the total_power method calculates the total power
> > consumption over different periods of time (a day, a month, or a year).
>
> > #### 1.2.2 Data part:
> >
> > There's sample data for 5 different devices (4 lamps for plant growing and 1 nas device)
> > 1 device is defined as a list of 4 elements:
> >
> > - name(str)
> > - power(float, unit: W)
> > - count(int, unit: ea)
> > - and use_time_a_day(int, unit: hour)
> >
> > These device data are stored in the data_list then Main part uses this list for calculating the total power
> > consumption.
>
> > #### 1.2.3 Main part:
> >
> > In this part, a list of Electrics objects is created from the data_list.
> > The total power consumption for each period of time (a day, a month, and a year) is then calculated and displayed as
> > the
> > result.

> ### 1.3 How to use for your own data
>
> Just change the Data part to your own data.
>
> > #### 1.3.1. Define your data as a list of 4 elements:
> >
> > your_any_data_name: list = [name(str), power(float, unit:W), cnt(int, unit(ea), use_time_a_day(int, unit:hour)]
> >
> > A name of data could be anything you want
> > But checkout the type and unit of each element
>
> > #### 1.3.2 Make data list from your data:
> >
> > Append your data in the data_list
>
> > #### 1.3.3 Run the code
> >
> > After you change the data, run the code and check the result

<br><br><br>

<a name="KoreanManual">

# 2. 한국어 설명서

</a>

> ### 1.1. 개요
>
> 전기기기들의 총 전력 소비량을 계산하는 파이썬 코드입니다.
> 이 코드는 세개의 파트로 나뉘어 있습니다.

> ### 1.2 각 파트별 안내
>
> > #### 1.2.1 Class 파트:
> >
> > Device, Electrics 클래스가 정의되어 있습니다. Device 클래스는 전기기기의 이름, 전력, 개수, 하루 사용시간을 인자로 받아 생성자 메소드를 실행합니다.
> > Electrics 클래스는 Device 클래스를 상속받아 daily_power, total_power 메소드를 추가합니다.
> >
> > daily_power 메소드는 하루 전력 소비량을 계산합니다. @property 데코레이터를 사용하여 메소드를 속성처럼 사용할 수 있습니다.
> > total_power 메소드는 a day, a month, a year 중 하나의 인자를 받아 해당 기간 동안의 전력 소비량을 계산합니다.
>
> > #### 1.2.2 Data 파트:
> >
> > 이 코드는 샘플 데이터를 포함하고 있습니다.
> >
> > 샘플 데이터는 4개의 식물등과 1개의 nas 기기의 정보를 담고 있습니다.
> >
> > 각 전기기기는 4개의 요소로 이루어진 리스트로 정의됩니다.
> >
> > - name(str)
> > - power(float, unit: W)
> > - count(int, unit: ea)
> > - and use_time_a_day(int, unit: hour)
> >
> > 각각의 정의된 전기기기 데이터는 data_list에 저장되고, Main 파트에서는 이 리스트를 사용하여 총 전력 소비량을 계산합니다.
> >
> > #### 1.2.3 Main 파트:
> >
> > data_list에 저장된 전기기기 데이터를 사용하여 Electrics 객체를 담고 잇는 리스트를 생성합니다.
> > 리스트를 순회하며 하루, 한달, 일년 동안의 전력 소비량을 계산하고 결과를 출력합니다.

> ### 1.3 본인의 데이터를 이용하여 계산하기
>
> Data 파트의 코드를 수정하여 실행합니다.
>
> > #### 1.3.1. 데이터를 4개의 요소로 정의합니다:
> >
> > your_any_data_name: list = [name(str), power(float, unit:W), cnt(int, unit(ea), use_time_a_day(int, unit:hour)]
> >
> > 데이터 변수의 이름은 자유롭게 설정하셔도 됩니다.
> > 다만 리스트 안 요소의 타입과 단위를 확인해주세요.
>
> > #### 1.3.2. 데이터를 data_list에 추가합니다:
> >
> > 1.3.1 에서 정의한 데이터 변수를 data_list에 추가합니다.
> >
> > #### 1.3.3 코드 실행
> >
> > 데이터 수정이 완료되었다면 코드를 실행하고 결과값을 출력합니다.
