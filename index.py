from src.services.eventsFetcher import getEventsBetween
import datetime as dt
from src.appConfig import initAppConfig
from src.services.emailSender import EmailSender
appConfig = initAppConfig()


hrsOffset = appConfig["hrsOffset"]
endDt = dt.datetime.now()
startDt = endDt-dt.timedelta(hours=hrsOffset)
dbConfig = appConfig["dbConfig"]
eventsDf = getEventsBetween(dbConfig, startDt, endDt)

if eventsDf.shape[0] > 0:
    # send email only if data is present
    dataFilePath = appConfig["dataFilePath"]
    eventsDf.to_excel(dataFilePath, index=False)
    # get all persons info
    persons = appConfig["persons"]
    emails = [p["email"] for p in persons]
    # send email
    startDtStr = dt.datetime.strftime(startDt, '%Y-%m-%d %H:%M:%S')
    endDtStr = dt.datetime.strftime(endDt, '%Y-%m-%d %H:%M:%S')
    subject = "events data from {0} to {1}".format(startDtStr, endDtStr)
    bodyHtml = "Please find attached the events data from {0} to {1}".format(
        startDtStr, endDtStr)
    emailConfig = appConfig["emailConfig"]
    emailApi = EmailSender(
        emailConfig["emailAddress"], emailConfig["username"],
        emailConfig["password"], emailConfig['host'])
    emailApi.sendEmail(emails, subject, bodyHtml, dataFilePath)
