FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade -y
RUN apt -y install exploitdb && apt -y install exploitdb-bin-sploits exploitdb-papers

ENTRYPOINT [ "searchsploit" ]
