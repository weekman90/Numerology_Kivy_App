import Numerology, kod, color, summkod, summdate, summyear, kodlastname, slovar
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', 1)  # window settings
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 600)
from kivy.uix.button import Button  # import kivy moduls
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Pythagoras matrix
matrix = {'1': '', '4': '', '7': '', '2': '', '5': '', '8': '', '3': '', '6': '', '9': ''}


# Body of kivy app
class MainApp (App):

    def build(self):

        # Main window for connect "submit"(Button of Result), "bl"
        self.mainbl = GridLayout(orientation='rl-bt', padding=5, spacing=10)
        self.mainbl.rows = 2

        # Layout for connect "self.matrixbox", "self.lb", "layout"
        bl = BoxLayout()

        # Layout for Pythagoras Matrix
        self.matrixbox = GridLayout(cols=3, size_hint=(.8, .4), spacing=2, orientation='tb-lr', padding=(0, -110, 0, 110))

        # Layout for Text inputs
        layout = GridLayout(cols=2, spacing=2)

        # Central Main Label
        self.lb = Label(size=['0.7', '1'], text='Нумеролог от Бога')

        # Create text inputs
        self.firstname = TextInput(text="", multiline=False)
        self.lastname = TextInput(text='', multiline=False)
        self.secondname = TextInput(text="", multiline=False)
        self.bday = TextInput(text="1", multiline=False)
        self.bmonth = TextInput(text="01", multiline=False)
        self.byear = TextInput(text="1990", multiline=False)
        self.street = TextInput(text="", multiline=False)
        self.house = TextInput(text="0", multiline=False)
        self.corps = TextInput(text="0", multiline=False)
        self.building = TextInput(text="0", multiline=False)
        self.appartment = TextInput(text="0", multiline=False)

        # Add text inputs and labels with name to layout
        layout.add_widget(Label(text='Имя', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.firstname)

        layout.add_widget(Label(text='Фамилия', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.lastname)

        layout.add_widget(Label(text='Отчество', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.secondname)

        layout.add_widget(Label(text='День рождения', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.bday)

        layout.add_widget(Label(text='Месяц рождения', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.bmonth)

        layout.add_widget(Label(text='Год рождения', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.byear)

        layout.add_widget(Label(text='Улица', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.street)

        layout.add_widget(Label(text='Дом', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.house)

        layout.add_widget(Label(text='Корпус', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.corps)

        layout.add_widget(Label(text='Строение', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.building)

        layout.add_widget(Label(text='Квартира', valign='center', halign='right', text_size=(100, 30)))
        layout.add_widget(self.appartment)

        # Empty widget near Reset button
        layout.add_widget(Widget())

        # Reset text Button
        layout.add_widget(Button(text='Отчистить',
                                 on_press=self.clear_textboxes))

        # Result Button
        submit = Button(text='Результат',
                        on_press=self.submit and self.result,
                        size_hint=(1, 0.15),
                        background_color="lightpink")

        # Build Main widget
        self.mainbl.add_widget(submit)
        bl.add_widget(self.matrixbox)
        bl.add_widget(self.lb)
        bl.add_widget(layout)
        self.mainbl.add_widget(bl)

        return self.mainbl

    # Business func
    def submit(self, obj):

        Numerology.firstname = (self.firstname.text.lower())
        Numerology.lastname = (self.lastname.text.lower())
        Numerology.secondname = (self.secondname.text.lower())
        Numerology.bday = (self.bday.text.lower())
        Numerology.bmonth = (self.bmonth.text.lower())
        Numerology.byear = (self.byear.text.lower())
        Numerology.street = (self.street.text.lower())
        Numerology.house = (self.house.text.lower())
        Numerology.corps = (self.corps.text.lower())
        Numerology.building = (self.building.text.lower())
        Numerology.appartment = (self.appartment.text.lower())
        Numerology.result = self

        self.firstname.text = 'Имя'
        self.lastname.text = 'Фамилия'
        self.secondname.text = 'Отчество'
        self.bday.text = "День рождения"
        self.bmonth.text = "Месяц рождения"
        self.byear.text = "Год рождения"
        self.street.text = "Улица"
        self.house.text = "№ дома"
        self.corps.text = "Корпус"
        self.building.text = "Строение"
        self.appartment.text = "№ квартиры"

    # Calculate logic
    def result(self, obj):
        try:
            self.matrixbox.clear_widgets()

            self.lb.text = f'KT : {color.color(str(self.firstname.text.lower()))},\n'

            self.lb.text += f'KF : ' \
                            f'{(kodlastname.kod(str(self.lastname.text.lower())))},\n'

            self.lb.text += f'KO : ' \
                            f'{kod.kod(self.secondname.text.lower())},\n'

            self.lb.text += f'KL : ' \
                            f'{summkod.summkod(self.firstname.text.lower(), self.secondname.text.lower(), self.lastname.text.lower())},\n'

            self.lb.text += f'KPV : ' \
                            f'{slovar.soglas(self.firstname.text.lower(), self.lastname.text.lower(), self.secondname.text.lower())},\n' \
                            f'KSP : {slovar.glassn(self.firstname.text.lower(), self.lastname.text.lower(), self.secondname.text.lower())},\n'

            self.lb.text += f'ЧДР :, {summdate.summ(self.bday.text.lower())},\n'

            self.lb.text += f'ЧМР :, {summdate.summ(self.bmonth.text.lower())},\n'

            self.lb.text += f'ЧГР :, {summdate.summ(self.byear.text.lower())},\n'

            self.lb.text += f'ЧЖП: ' \
                            f'{summyear.чжп(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())},\n'

            self.lb.text += f'KR: ' \
                            f'{summdate.summwith(str(int(summyear.чжп(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())) + int(kod.kod(self.firstname.text.lower())) + int(kod.kod(self.secondname.text.lower())) + int(kod.kod(self.lastname.text.lower()))))},\n'

            self.lb.text += f'Второй чилсовой ряд A : ' \
                            f'{summyear.First_number_row(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())},\n'

            self.lb.text += f'Второй чилсовой ряд B : ' \
                            f'{summyear.чжп2(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())},\n'

            self.lb.text += f'Второй чилсовой ряд C : ' \
                            f'{int(summyear.First_number_row(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())) - int(summyear.bday0(self.bday.text.lower()))},\n'

            self.lb.text += f'Второй чилсовой ряд D : ' \
                            f'{summyear.bday0summ(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())},\n'

            self.lb.text += f'Код улицы : ' \
                            f', {kod.kod(self.street.text.lower())},\n'

            self.lb.text += f'Код № дома с корп. и стр. : ' \
                            f'{summdate.summ(summdate.summ(self.house.text.lower()) + summdate.summ(self.corps.text.lower()) + summdate.summ(self.building.text.lower()))},\n'

            self.lb.text += f'Код № квартиры : {summdate.summ(self.appartment.text.lower())},\n'

            self.lb.text += f'Код места проживания : ' \
                            f'{summdate.summ(str(int(kod.kod(self.street.text.lower())) + int(summdate.summ(self.appartment.text.lower())) + int(summdate.summ(summdate.summ(self.house.text.lower()) + summdate.summ(self.corps.text.lower()) + summdate.summ(self.building.text.lower())))))},\n'

            matrix = {'1': '', '4': '', '7': '', '2': '', '5': '', '8': '', '3': '', '6': '', '9': ''}

            fulldate = (self.bday.text.lower() + self.bmonth.text.lower() + self.byear.text.lower())

            second_number_row = \
                str(summyear.First_number_row
                    (self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())) + str(
                    summyear.чжп2(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower()))\
                + str(int(summyear.First_number_row
                          (self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower())) -
                      int(summyear.bday0(self.bday.text.lower())))\
                + str(summyear.bday0summ(self.bday.text.lower(), self.bmonth.text.lower(), self.byear.text.lower()))
            fulldate = fulldate + second_number_row

            for i in fulldate:
                if i in matrix.keys():
                    for j in matrix.keys():
                        if i == j:
                            matrix[i] += j

            # Reset text in Matrix
            self.matrixbox.add_widget(Button(text=f'{(matrix["1"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["2"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["3"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["4"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["5"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["6"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["7"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["8"])}'))
            self.matrixbox.add_widget(Button(text=f'{(matrix["9"])}'))

            return self

        except:
            self.matrixbox.clear_widgets()
            self.lb.text = 'В полях:\n\nИмя,Фамилия,Отчество,Улица- \n\n' \
                           'Используйте\nКириллицу или Латиницу,\n\n\n' \
                           'В полях:\n\nДень рождения,\nМесяц рождения, Год рождения,\n' \
                           'Дом, Корпус, Строение, Квартира -\n\nИспользуйте цифры.'

    # Reset text in text-boxes func.
    def clear_textboxes(self, obj):

        self.firstname.text = ''
        self.lastname.text = ''
        self.secondname.text = ''
        self.bday.text = "1"
        self.bmonth.text = "01"
        self.byear.text = "1990"
        self.street.text = ""
        self.house.text = "0"
        self.corps.text = "0"
        self.building.text = "0"
        self.appartment.text = "0"


if __name__ == '__main__':
    MainApp().run()
