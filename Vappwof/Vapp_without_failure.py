def Vapp_without_failure(vls, appr_cor):
    Vapp = vls + appr_cor
    return Vapp

def determine_vls(weight):
    vls_conf3 = ""
    vls_conf_full = ""

    if weight < 96000:
        print('Please enter a valid landing weight')
    if weight >= 96000 and weight < 102000:
        vls_conf_full = int(110)
        vls_conf_3 = int(113)
    elif weight >= 102000 and weight < 110000:
        vls_conf_full = int(114)
        vls_conf_3 = int(117)
    elif weight >= 110000 and weight < 118000:
        vls_conf_full = int(118)
        vls_conf_3 = int(121)
    elif weight >= 118000 and weight < 126000:
        vls_conf_full = int(122)
        vls_conf_3 = int(126)
    elif weight >= 126000 and weight < 134000:
        vls_conf_full = int(126)
        vls_conf_3 = int(130)
    elif weight >= 134000 and weight < 142000:
        vls_conf_full = int(130)
        vls_conf_3 = int(134)
    elif weight >= 142000 and weight < 150000:
        vls_conf_full = int(134)
        vls_conf_3 = int(138)
    elif weight >= 150000 and weight <158000:
        vls_conf_full = int(138)
        vls_conf_3 = int(141)
    elif weight >= 158000 and weight < 166000:
        vls_conf_full = int(141)
        vls_conf_3 = int(145)
    elif weight >= 166000 and weight < 172000:
        vls_conf_full = int(145)
        vls_conf_3 = int(149)
    else:
        vls_conf_full = int(147)
        vls_conf_3 = int(152)
    print(vls_conf3)

determine_vls(142000)


"""def determine_appr_cor():
    config = ""
    appr_cor = int("")
    autothrust_on = input('Is A/THR engaged? Y/n').lower()
    ice_accretion = input('Is there any ice accretion? Y/n').lower()
    while True:
        if not autothrust_on == 'y':
            continue
        else:
            appr_cor = 5
        if not ice_accretion == 'y':
            continue
        else:
            appr_cor = 5"""










