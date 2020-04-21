import mailbox
import csv


def convert_to_csv(mbox_file, csv_file):
    writer = csv.writer(open(csv_file, 'w'))
    writer.writerow(["from", "subject", "date", "body"])

    for message in mailbox.mbox(mbox_file):
        body = None
        if message.is_multipart():
            for part in message.walk():
                if part.is_multipart():
                    for subpart in part.walk():
                        if subpart.get_content_type() == 'text/plain':
                            body = subpart.get_payload(decode=True)
                elif part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
        elif message.get_content_type() == 'text/plain':
            body = message.get_payload(decode=True)
        if body:
            body = body.decode('utf-8')

        writer.writerow([message['from'], message['subject'], message['date'], body])


if __name__ == "__main__":
    mbox_filename = input('enter mbox filename(.mbox)')
    csv_filename = input('enter output filename (.csv)')
    convert_to_csv(mbox_filename, csv_filename)
