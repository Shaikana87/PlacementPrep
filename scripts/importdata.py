from Dashboard.models import Questions, Domain 
# from Dashboard.models import Questions, Domain 
import csv

def run():
    with open('scripts/lovebabbar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Questions.objects.all().delete()
        Domain.objects.all().delete()

        for row in reader:
            # print(row)

            domain, _ = Domain.objects.get_or_create(domain_name=row[4])
            domain.save()
            # print(domain)

            questions = Questions(que_id=row[0],
                                que_title=row[2],
                                que_link=row[3],
                                # que_domain=domain,
                                que_difficulty=row[5],
                                dsa_sheet=row[6])

            # questions.que_domain.set(domain)
            questions.save()
            questions.que_domain.add(domain)