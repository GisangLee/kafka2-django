# Generated by Django 4.1.4 on 2023-01-26 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("deleted", models.DateTimeField(db_index=True, editable=False, null=True)),
                ("deleted_by_cascade", models.BooleanField(default=False, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
            ],
            options={
                "verbose_name": "채팅",
                "verbose_name_plural": "채팅",
                "db_table": "chat",
                "ordering": ["-updated_at", "-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("deleted", models.DateTimeField(db_index=True, editable=False, null=True)),
                ("deleted_by_cascade", models.BooleanField(default=False, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("text", models.TextField(blank=True, null=True, verbose_name="텍스트")),
                ("image", models.URLField(blank=True, null=True, verbose_name="이미지")),
                (
                    "chat",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="chat.chat", verbose_name="채팅"),
                ),
            ],
            options={
                "verbose_name": "메세지",
                "verbose_name_plural": "메세지",
                "db_table": "message",
                "ordering": ["-created_at"],
            },
        ),
    ]
