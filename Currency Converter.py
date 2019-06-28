from tkinter import *
master = Tk()
master.title("Currency Converter")
master.geometry("600x400")

rates = {"Cuban Convertible Peso": 0.0144495298, "Saint Helenian Pound": 0.0110789003, "Seychellois Rupee": 0.2021331439, "Bulgarian Lev": 0.0251910684, "Comorian Franc": 6.3365390851, "Moldovan Leu": 0.2504109833, "Bosnian Convertible Marka": 0.0251910684, "Macau Pataca": 0.1168251279, "New Zealand Dollar": 0.0212342789, "Burundian Franc": 26.3506934109, "Indonesian Rupiah": 205.7682162588, "Icelandic Krona": 1.7729593534, "Kyrgyzstani Som": 1.0092939019, "Iranian Rial": 607.2460933294, "Euro": 0.0128799887, "Mozambican Metical": 0.9194193464, "Afghan Afghani": 1.0965734298, "Paraguayan Guarani": 89.3691162531, "Guernsey Pound": 0.0110789003, "Pakistani Rupee": 2.0256350891, "Cuban Peso": 0.3829125397, "Bahamian Dollar": 0.0144495298, "Moroccan Dirham": 0.1395160347, "Danish Krone": 0.095654406, "Bahraini Dinar": 0.0054330232, "Kazakhstani Tenge": 5.4820867396, "Maldivian Rufiyaa": 0.2264124104, "Lebanese Pound": 21.7826661719, "British Pound": 0.0110789003, "Samoan Tala": 0.0381454254, "Dominican Peso": 0.7311492038, "Croatian Kuna": 0.0957066873, "Ukrainian Hryvnia": 0.3961245933, "Thai Baht": 0.4582720688, "Japanese Yen": 1.601904749, "Malagasy Ariary": 51.6312678404, "US Dollar": 0.0144495298, "Guinean Franc": 132.2884850656, "Swedish Krona": 0.1343957877, "Iraqi Dinar": 17.1983808933, "Brazilian Real": 0.0566906128, "Nepalese Rupee": 1.6075, "Tunisian Dinar": 0.0437318104, "Cape Verdean Escudo": 1.4202763594, "Bermudian Dollar": 0.0144495298, "Swazi Lilangeni": 0.2094227603, "Romanian Leu": 0.0614221988, "Costa Rican Colon": 8.7044429191, "Somali Shilling": 8.3810623029, "CFP Franc": 1.5369914976, "Aruban or Dutch Guilder": 0.0258646583, "Seborgan Luigino": 0.002408255, "Haitian Gourde": 1.1984533428, "Philippine Peso": 0.7613604479, "Cambodian Riel": 57.510515489, "Libyan Dinar": 0.0200815391, "Hungarian Forint": 4.1355868864, "Australian Dollar": 0.0203615963, "Salvadoran Colon": 0.1264333857, "Indian Rupee": 1.0, "Congolese Franc": 23.6957842686, "Argentine Peso": 0.6254661193, "Belizean Dollar": 0.0291201069, "Sudanese Pound": 0.6879608635, "Angolan Kwanza": 4.597029025, "Jordanian Dinar": 0.0102447166, "Mauritanian Ouguiya": 0.5289967169, "Barbadian or Bajan Dollar": 0.0288990596, "Czech Koruna": 0.3325308089, "Ethiopian Birr": 0.4157193968, "Sao Tomean Dobra": 0.3149879236, "Hong Kong Dollar": 0.1134224543, "Rwandan Franc": 12.8415798718, "Turkish Lira": 0.0803852456, "Trinidadian Dollar": 0.097682104, "South Korean Won": 16.4180153575, "Sierra Leonean Leone": 125.7109093004, "Emirati Dirham": 0.0530658982, "Colombian Peso": 46.0364367915, "Sri Lankan Rupee": 2.5354906099, "Kenyan Shilling": 1.4551033887, "Botswana Pula": 0.155874201, "Silver Ounce": 0.0009548502, "Egyptian Pound": 0.2501612381, "Bolivian Bol\u00edviano": 0.1002062565, "Palladium Ounce": 1.0497e-05, "Uzbekistani Som": 121.3616007792, "Solomon Islander Dollar": 0.1160602797, "Guatemalan Quetzal": 0.1110011719, "Mexican Peso": 0.2808197828, "Venezuelan Bol\u00edvar": 47.4854801632, "Zambian Kwacha": 0.1765765404, "Panamanian Balboa": 0.0144495298, "Nicaraguan Cordoba": 0.4739443337, "Serbian Dinar": 1.5181713693, "Central African CFA Franc BEAC": 8.4487187802, "Georgian Lari": 0.0389689353, "Burmese Kyat": 21.8611216391, "Surinamese Dollar": 0.1071450651, "Tongan Pa'anga": 0.0336036929, "Omani Rial": 0.0055558442, "Malaysian Ringgit": 0.0589959814, "Bruneian Dollar": 0.0197254199, "Eritrean Nakfa": 0.216742947, "Liberian Dollar": 2.3770920674, "CFA Franc": 8.4487187802, "Tajikistani Somoni": 0.1363847729, "Namibian Dollar": 0.2094227603, "Honduran Lempira": 0.3529308761, "Basotho Loti": 0.2094227603, "Ghanaian Cedi": 0.0784681836, "Swiss Franc": 0.0143806277, "Bangladeshi Taka": 1.2173078162, "Azerbaijan Manat": 0.0245642013, "Platinum Ounce": 1.70214e-05, "Djiboutian Franc": 2.5720111457, "Chilean Peso": 9.8329774018, "IMF Special Drawing Rights": 0.0104084494, "Norwegian Krone": 0.1248366208, "South African Rand": 0.2094227603, "Tanzanian Shilling": 33.4008436828, "Nigerian Naira": 5.2016224937, "North Korean Won": 13.0055159043, "Albanian Lek": 1.6132899242, "Mauritian Rupee": 0.5097762035, "Vietnamese Dong": 335.3019618877, "Chinese Yuan Renminbi": 0.0969719128, "Falkland Island Pound": 0.0110789003, "Guyanese Dollar": 3.007885314, "Yemeni Rial": 3.6073536358, "Qatari Riyal": 0.0525962885, "Canadian Dollar": 0.0192789687, "Caymanian Dollar": 0.0118486143, "Gambian Dalasi": 0.7185740456, "Russian Ruble": 0.9644283082, "Macedonian Denar": 0.7901056548, "Taiwan New Dollar": 0.4463317374, "Dutch Guilder": 0.0258140847, "Tuvaluan Dollar": 0.0203615963, "Polish Zloty": 0.0554576883, "Mongolian Tughrik": 37.7638461322, "Ugandan Shilling": 53.679902149, "Algerian Dinar": 1.7356096631, "Jamaican Dollar": 1.7877959674, "Saudi Arabian Riyal": 0.0541857367, "Papua New Guinean Kina": 0.048733794, "Syrian Pound": 7.4446024529, "Ni-Vanuatu Vatu": 1.6288955432, "Bhutanese Ngultrum": 1.0, "Gibraltar Pound": 0.0110789003, "Gold Ounce": 1.11824e-05, "Peruvian Sol": 0.0479292143, "Singapore Dollar": 0.0197254199, "Kuwaiti Dinar": 0.0044013228, "Uruguayan Peso": 0.488031723, "Jersey Pound": 0.0110789003, "Malawian Kwacha": 10.5703277238, "Lao Kip": 124.4696199732, "Fijian Dollar": 0.0307775536, "Zimbabwean Dollar": 5.2292848342, "Armenian Dram": 7.0288293106, "East Caribbean Dollar": 0.0390494254, "Turkmenistani Manat": 0.0505733543, "Israeli Shekel": 0.0525086438, "Belarusian Ruble": 0.0307052508, "Isle of Man Pound": 0.0110789003}
currency = []
for i in rates:
    currency.append(i)
currency.sort()

def on_keyrelease(event):
    value = event.widget.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = currency
    else:
        data = []
        for item in currency:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    w3.delete(0, 'end')

    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        w3.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')


heading = Label(master, text="Currency Converter",
                font="Verdana 20 bold")
amt = Label(master, text="Amount : ")


value = Entry(master)

result = Label(master, text="",
               font="Times 12 bold")

fromc = Label(master, text="From : ")

fromCur = StringVar(master)
fromCur.set(currency[71]) # default value

w1 = OptionMenu(master, fromCur, *currency)

toc = Label(master, text="To : ")
toCur = StringVar(master)
toCur.set(currency[-10]) # default value

w2 = OptionMenu(master, toCur, *currency)

'''
entry = Entry(master)
entry.grid(row=5, column=1)
entry.bind('<KeyRelease>', on_keyrelease)

w3 = Listbox(master)
#w3.grid(row=6, column=1)

w3.bind('<<ListboxSelect>>', on_select)
listbox_update(currency)
'''

def convert():
    try:
        float(value.get())
        a = rates[fromCur.get()]
        b = rates[toCur.get()]

        res = float(value.get())*b/a
        result.configure(text = "Value: " + str(round(res,3)))
    except ValueError:
        result.configure(text = "Not a correct format")
    

def refreshVal():
    pass

conButton = Button(master, text="Convert", command=convert,
                   font="Verdana 13 bold")

refresh = Button(master, text="Refresh", command=refreshVal)

comments = Label(master, text="Comments: Not connected to internet now. Showing old values.")

def griding():
    heading.grid()
    amt.grid(row=0, column=0)
    value.grid(row=0, column=1)
    result.grid(row=2, column=1)
    fromc.grid(row=3, column=0)
    toc.grid(row=4, column=0)
    w1.grid(row=3, column=1)
    w2.grid(row=4, column=1)
    conButton.grid(row=7, column=1)
    refresh.grid(row=8, column=2)
    comments.grid(row=9, column=1)

def placing():
    heading.place(x=160)
    
    amt.place(x=175, y=60)
    value.place(x=240, y=60)

    result.place(x=240, y=100)

    fromc.place(x=80, y=155)
    w1.place(x=125, y=150)
    
    toc.place(x=320, y=155)
    w2.place(x=350, y=150)

    conButton.place(x=230, y=240)
    refresh.place(x=250, y=320)

    comments.place(x=70, y=370)
    
placing()
master.mainloop()
