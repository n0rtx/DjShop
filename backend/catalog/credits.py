COMMONS = "https://commons.wikimedia.org/wiki/File:"

PHOTO_CREDITS = {
    "akai-mpc-live": ("Joan Recordà", "CC BY-SA 4.0", "Akai_MPC_Live_(2017).jpg"),
    "akai-mpc-studio": ("Matt Vanacoro, Clusternote", "CC BY 3.0", "Akai_MPC_Studio_(front).jpg"),
    "audio-technica-ath-m50": ("Fletcher6", "CC BY 4.0", "Audio_Technica_ATH-M50_Headphones.jpg"),
    "beyerdynamic-dt-770-pro": ("MMuzammils", "CC BY-SA 3.0", "Beyerdynamic_DT_770_PRO_80_Ohm_-01.JPG"),
    "pioneer-dj-club-bundle": ("FASTILY", "CC BY-SA 4.0", "CDJ-2000_Nexus_%26_DJM-900_1_2023-11-14.jpg"),
    "pioneer-cdj-2000": ("Fabexplosive", "CC BY-SA 3.0", "CDJ_2000.jpg"),
    "reloop-rp-1000-mk3": ("muzyczny.pl", "CC BY-SA 4.0", "Gramofon_RP-1000MK3_firmy_Reloop.jpg"),
    "krk-rokit-5": ("TaurusEmerald", "CC BY-SA 4.0", "KRK_Rokit_5.jpg"),
    "traktor-kontrol-s4-mk3": ("Russomc", "CC BY-SA 4.0", "Native-instruments-traktor-kontrol-s4-mk3.jpg"),
    "numark-mixtrack-pro": ("Raidarmax", "CC BY-SA 3.0", "Numark_Mixtrack_Pro_DJ_Controller.jpg"),
    "pioneer-ddj-flx4": ("Solomon203", "CC BY-SA 4.0", "Pioneer_DDJ-FLX4_at_Taipei_Media_School_booth_20250810.jpg"),
    "pioneer-ddj-rx": ("Jonn Leffmann", "CC BY 3.0", "Pioneer_DDJ-RX_DJ-Controller_(front)_with_computer_running_mixing_software_Rekordbox.jpg"),
    "pioneer-djm-350": ("Natanarkia", "CC BY-SA 4.0", "Pioneer_DJM-350_20181003.jpg"),
    "pioneer-djm-600": ("galki", "CC BY 2.0", "Pioneer_DJM-600_in_Japan_(3476350726).jpg"),
    "pioneer-djm-900-booth": ("Pete Brown", "CC BY 2.0", "Pioneer_DJM-900_Nexus_2013-06-27.jpg"),
    "pioneer-ddj-rev1": ("TaurusEmerald", "CC BY-SA 4.0", "Pioneer_DJ_DDJ-REV1.jpg"),
    "pioneer-xdj-aero": ("Lukas Plewnia", "CC BY-SA 2.0", "Pioneer_XDJ-AERO_in_IFA_20130907.jpg"),
    "reloop-rhp-20": ("Leslie Jones", "CC BY 2.0", "Reloop_RHP-20_headphone.jpg"),
    "sennheiser-hd-25": ("Bizzarle", "CC BY-SA 4.0", "Sennheiser_hd-25_headphones.jpg"),
    "shure-beta-58a": ("Geheimnisträgerin", "CC BY-SA 3.0", "ShureBeta58A.jpg"),
    "shure-sm58": ("Iain Fergusson, Binksternet", "CC BY 2.5", "Shure_SM58.jpg"),
    "shure-sm58-closeup": ("ChrisHH", "CC BY-SA 3.0", "Shure_sm58.jpg"),
    "reloop-slipmat": ("muzyczny.pl", "CC BY-SA 4.0", "Slipmata_Spin_me_round!_firmy_Reloop.jpg"),
    "technics-sl-1200-mk2": ("Dydric, 32bitmaschine", "CC BY-SA 2.5", "Technics_SL-1200MK2-2.jpg"),
    "technics-sl-1210-mk2": ("jayniebell", "CC BY 2.0", "Technics_SL-1210Mk2.jpg"),
    "technics-sl-1200-mk5": ("MärkJ2057", "CC BY-SA 4.0", "Technics_sl-1200_mk5.jpg"),
    "traktor-kontrol-s4-mk2": ("Mriya127", "CC BY-SA 4.0", "Traktor_Kontrol_S4_MK2.jpg"),
    "cdj-nxs2-setup": ("加蛋不加價", "CC BY 2.0", "Pioneer_CDJ-2000NXS2_DJM-900NXS2_at_PPP_(50763452917).jpg"),
    "ddj-sx-outdoor": ("Cjp24", "CC BY-SA 4.0", "Printemps_de_Bourges_2019-15,_contr%C3%B4leur_DJ.jpg"),
    "club-booth": ("Arnold Jaeger Werner", "CC BY 2.0", "Three_CDJs_and_two_SL-1210_at_Bob_Beaman_Nightclub_Munich.jpg"),
    "tresor-turntable": ("Angie Linder", "CC BY-SA 2.0", "Tresor_Nightclub_Berlin_DJ_Gear_Slipmat_BW.jpg"),
}


def credit(slug):
    author, license_name, file_name = PHOTO_CREDITS[slug]
    return {"author": author, "license": license_name, "source": f"{COMMONS}{file_name}", "provider": "Wikimedia Commons"}
