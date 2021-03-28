import shellcolor

print(
    shellcolor.shellcolor('attention',
                          forecolor='yellow',
                          backcolor='red',
                          bold=True,
                          ) + ' : ' +
    shellcolor.shellcolor('today is your day',
                          forecolor='magenta',
                          backcolor='grey',
                          italic=True
                          )
)
