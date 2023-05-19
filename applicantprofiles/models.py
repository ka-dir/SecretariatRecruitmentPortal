from django.db import models


# Create your models here.

class BioData(models.Model):
    surname = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    other_name = models.CharField(max_length=32, blank=True, null=True)
    salutation = models.CharField(max_length=64, blank=True, null=True)
    id_number = models.CharField('ID Number', max_length=64, blank=True, null=True)
    dob = models.CharField('Date of Birth', max_length=64, blank=True, null=True)
    upload_id = models.ImageField('Upload Identification Document (ID/Passport)', blank=True, null=True)
    tsc_no = models.CharField('TSC Number', max_length=12, blank=True, null=True)
    kra_pin = models.CharField('KRA PIN', max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)
    marital_status = models.CharField(max_length=11, blank=True, null=True)
    nationality_at_birth = models.CharField(max_length=24, blank=True, null=True)
    current_nationality = models.CharField(max_length=24, blank=True, null=True)
    legal_residency = models.CharField(max_length=24, blank=True, null=True)
    county = models.CharField(max_length=11, blank=True, null=True)
    subcounty = models.CharField(max_length=11, blank=True, null=True)
    constituency = models.CharField(max_length=11, blank=True, null=True)
    postal_address = models.CharField(max_length=11, blank=True, null=True)
    postal_code = models.CharField(max_length=11, blank=True, null=True)
    postal_town = models.CharField(max_length=11, blank=True, null=True)
    phone_no = models.CharField('Phone Number', max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True)
    disability_status = models.CharField(max_length=32, blank=True, null=True)
    disability_desc = models.CharField('Disability Description', max_length=32, blank=True, null=True)
    disability_no = models.CharField('Disability Registration Number', max_length=32, blank=True, null=True)
    disability_reg_date = models.CharField('Disability Registration Date', max_length=32, blank=True, null=True)
    conviction_status = models.CharField(max_length=32, blank=True, null=True)
    conviction_desc = models.CharField('Conviction Description', max_length=32, blank=True, null=True)
    dismissal_status = models.CharField(max_length=32, blank=True, null=True)
    dismissal_desc = models.CharField('Dismissal Description', max_length=32, blank=True, null=True)
    dismissal_date = models.CharField('Dismissal Date', max_length=32, blank=True, null=True)
    corruption_status = models.CharField(max_length=32, blank=True, null=True)
    corruption_desc = models.CharField(max_length=32, blank=True, null=True)
    current_employer = models.CharField(max_length=64, blank=True, null=True)
    position_held = models.CharField(max_length=32, blank=True, null=True)
    start_date = models.CharField(max_length=32, blank=True, null=True)
    still_working = models.BooleanField(default=True, blank=True, null=True)
    end_date = models.CharField(max_length=32, blank=True, null=True)
    gross_salary = models.CharField(max_length=32, blank=True, null=True)

    surname_contact_person = models.CharField(max_length=32, blank=True, null=True)
    first_contact_person = models.CharField(max_length=32, blank=True, null=True)
    other_contact_person = models.CharField(max_length=32, blank=True, null=True)
    relationship_to_contact_person = models.CharField(max_length=32, blank=True, null=True)
    mobile_no_contact_person = models.CharField(max_length=32, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'BioData'
        verbose_name_plural = 'BioData'

    def __str__(self):
        return '{} ' '{} ' '{} '.format(self.surname, self.first_name, self.other_name)


class AcademicQualification(models.Model):
    degree_level = models.CharField('Degree level', max_length=64, blank=True, null=True)
    degree_obtained = models.CharField('Diploma/degree obtained', max_length=64, blank=True, null=True)
    start = models.CharField(max_length=64, blank=True, null=True)
    to = models.CharField(max_length=64, blank=True, null=True)
    main_field_of_study = models.CharField('Main field of study', max_length=64, blank=True, null=True)
    university_institution = models.CharField('University/Institution', max_length=64, blank=True, null=True)
    other_university_institution = models.CharField('Other university', max_length=64, blank=True, null=True)
    upload_cert = models.ImageField('Upload supporting document(s). For example, degree, diploma or certificate.',
                                    blank=True, null=True)
    certificate_number = models.ImageField('Certificate number', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} ' '{} '.format(self.degree_level, self.degree_obtained, self.university_institution)


class CriminalOffence(models.Model):
    conviction_status = models.BooleanField(
        'Have you ever been convicted of any criminal offence or a subject of probation order?', default=False,
        blank=True, null=True)
    conviction_reason = models.CharField(max_length=255, blank=True, null=True)
    removed_from_employment_status = models.BooleanField(
        'Have you ever been dismissed or otherwise removed from employment ?', default=False, blank=True, null=True)
    removed_from_employment_reason = models.CharField(max_length=255, blank=True, null=True)
    corruption_case_status = models.BooleanField('Do you have any ongoing criminal or corruption case ? ',
                                                 default=False, blank=True, null=True)
    corruption_case_status_reason = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} ' '{} '.format(self.conviction_reason, self.removed_from_employment_reason,
                                        self.corruption_case_status_reason)


class ProfessionalQualification(models.Model):
    degree_level = models.CharField('Degree level', max_length=64, blank=True, null=True)
    degree_obtained = models.CharField('Diploma/degree obtained', max_length=64, blank=True, null=True)
    start = models.CharField(max_length=64, blank=True, null=True)
    to = models.CharField(max_length=64, blank=True, null=True)
    main_field_of_study = models.CharField('Main field of study', max_length=64, blank=True, null=True)
    university_institution = models.CharField('University/Institution', max_length=64, blank=True, null=True)
    other_university_institution = models.CharField('Other university', max_length=64, blank=True, null=True)
    upload_cert = models.ImageField('Upload supporting document(s). For example, degree, diploma or certificate.',
                                    blank=True, null=True)
    certificate_number = models.ImageField('Certificate number', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} ' '{} '.format(self.degree_level, self.degree_obtained, self.university_institution)


class RelevantCourse(models.Model):
    start = models.CharField(max_length=64, blank=True, null=True)
    to = models.CharField(max_length=64, blank=True, null=True)
    university_institution = models.CharField('University/Institution', max_length=64, blank=True, null=True)
    other_university_institution = models.CharField('Other university', max_length=64, blank=True, null=True)
    name_of_the_course = models.CharField(max_length=128, blank=True, null=True)
    upload_cert = models.ImageField('Upload supporting document(s). For example, degree, diploma or certificate.',
                                    blank=True, null=True)
    certificate_number = models.ImageField('Certificate number', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} '.format(self.university_institution, self.name_of_the_course)


class MembershipProfessionalBody(models.Model):
    professional_body = models.CharField(max_length=128, blank=True, null=True)
    registration_number = models.CharField(max_length=128, blank=True, null=True)
    membership_type = models.CharField(max_length=24, blank=True, null=True)
    upload_cert = models.ImageField('Upload supporting document(s). For example,certificate.',
                                    blank=True, null=True)
    date_of_renewal = models.CharField(max_length=12, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'MembershipProfessionalBody'
        verbose_name_plural = 'MembershipProfessionalBodies'

    def __str__(self):
        return '{} ' '{} '.format(self.professional_body, self.registration_number)


class ProfessionalExperience(models.Model):
    start = models.CharField(max_length=128, blank=True, null=True)
    to = models.CharField(max_length=128, blank=True, null=True)
    until_now = models.BooleanField(default=True, blank=True, null=True)
    position_title = models.CharField(max_length=128, blank=True, null=True)
    gross_monthly_salary = models.BigIntegerField(blank=True, null=True)
    employer_organization = models.CharField('Employer/Organization', max_length=64, blank=True, null=True)
    description_of_major_activities = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} '.format(self.position_title, self.employer_organization)


class Reference(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    referee_role_or_position = models.CharField(max_length=128, blank=True, null=True)
    direct_supervisor = models.BooleanField(default=False, blank=True, null=True)
    email_address = models.EmailField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    preferred_correspondence_language = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ' '{} '.format(self.name, self.referee_role_or_position)
