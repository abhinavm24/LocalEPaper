from crontab import CronTab

# https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231

# cron gyan
# https://serverfault.com/questions/449651/why-is-my-crontab-not-working-and-how-can-i-troubleshoot-it

my_cron = CronTab(user='gugli')
def main():
	remove_chron()
	add_chron('cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/Dainik_e_paper.py')


def remove_chron():
	for job in my_cron:
		my_cron.remove(job)
		my_cron.write()

def add_chron(cmd):
	job = my_cron.new(command= cmd, comment='e_dainik_jagron' )
	#wrinting cron job to cron tab
	my_cron.write()

	#scheduling the job
	job.minute.every(1) 


	## MANUALLY UPDATED crontab (`crontab -e`) the frequecy * */2 * * * [ at interval of 2 hrs atarting from 0000]


if __name__ == "__main__":
    main()
