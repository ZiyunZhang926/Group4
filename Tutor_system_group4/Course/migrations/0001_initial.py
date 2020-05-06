# Generated by Django 3.0.3 on 2020-05-05 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_Profile', '0004_auto_20200505_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=50)),
                ('grade_course', models.CharField(choices=[('0', '小学一年级至三年级'), ('1', '小学四年级至六年级'), ('2', '初一'), ('3', '初二'), ('4', '初三'), ('5', '高一'), ('6', '高二'), ('7', '高三'), ('8', '其他')], max_length=2)),
                ('subject', models.CharField(choices=[('zh', '语文'), ('math', '数学'), ('en', '英语'), ('phy', '物理'), ('che', '化学'), ('bio', '生物'), ('pol', '政治'), ('his', '历史'), ('geo', '地理')], max_length=10)),
                ('comment', models.CharField(default='', max_length=100)),
                ('state_match', models.BooleanField()),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User_Profile.Student')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User_Profile.Teacher')),
            ],
        ),
    ]