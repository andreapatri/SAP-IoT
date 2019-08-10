import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("demoinventorysap@gmail.com", "SAPSAP2017")

msg = "YOUR MESSAGE! OHHH www.facebook.com "
server.sendmail("demoinventorysap@gmail.com", "demoinventorysap@gmail.com", msg)
server.quit()
