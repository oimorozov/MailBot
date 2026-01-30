import time
from email import message_from_bytes
from email.header import decode_header
from imaplib import IMAP4_SSL
from config import USER_NAME, IMAP_PASS

def get_mail():
    mails: list[tuple[str, str]] = []
    with IMAP4_SSL("imap.yandex.ru") as imap:
        try:
            imap.login(user=USER_NAME, password=IMAP_PASS)
            imap.select("INBOX")
            status, args = imap.noop()  
            if status != "OK":
                raise Exception()

            _, args = imap.search(None, "ALL")
            for num in list(reversed(args[0].split()))[:5]:
                _, data = imap.fetch(num, "(RFC822)")
                mail = message_from_bytes(data[0][1])
                decode_args = decode_header(mail["Subject"])
                from_args = decode_header(mail["From"])

                decode_from = ""
                for part, decoding in from_args:
                    if decoding == "utf-8":
                        decode_from = part.decode("utf-8")
                    elif decoding == "windows-1251":
                        decode_from = part.decode("windows-1251")
                    elif decoding == "koi8-r":
                        decode_from = part.decode("koi8-r")
                    elif decoding == None:
                        decode_from = part
                    else:
                        raise Exception(f"Expected {decoding=}")
                    decode_from = str(decode_from)[2:-1]
                    print(f"{decode_from=} ")
                decode_subject = ""
                for part, decoding in decode_args:
                    if decoding == "utf-8":
                        decode_subject = part.decode("utf-8")
                    elif decoding == "windows-1251":
                        decode_subject = part.decode("windows-1251")
                    elif decoding == "koi8-r":
                        decode_from = part.decode("koi8-r")
                    elif decoding == None:
                        decode_subject = part
                    else:
                        raise Exception(f"Expected {decoding=}")
                
                mails.append((decode_from, decode_subject))

                print(f"Message #{num}, content: {decode_subject}")
                time.sleep(1)
            return mails
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    get_mail()