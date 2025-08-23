from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=500)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tool', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill proficiency percentage (0-100)"
    )
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-end_date', '-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class PersonalInfo(models.Model):
    """
    Personal information for Smarika Tripathi:
    - Name: Smarika Tripathi
    - Title: Computer Engineering Student at Pokhara University
    - Bio: Third-year Computer Engineering student passionate about web development, biometric authentication, and IoT-based solutions. Actively learning full-stack development, embedded systems, and AI/ML. Open to internships, collaborations, and research opportunities.
    - Email: smarikatripathi1@gmail.com
    - LinkedIn: https://www.linkedin.com/in/smarika-tripathi-305273257/
    - GitHub: https://github.com/Smarikatripathi
    """
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    primary_color = models.CharField(max_length=7, default='#007bff')
    secondary_color = models.CharField(max_length=7, default='#6c757d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Personal Info" 