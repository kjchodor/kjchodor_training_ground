mapa = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    * 
                    **     *                    *
...................................................................."""

znaki_podane = input("podaj tekst lub znaki: ")

pozycja = 0

for x in mapa:
    if x not in " \r\n":
       print(znaki_podane[pozycja], end = "")
    else:
       print(x, end = "")
    pozycja = pozycja + 1
    if pozycja >= len(znaki_podane):
        pozycja = 0