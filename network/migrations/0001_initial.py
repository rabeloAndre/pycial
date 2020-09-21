# Generated by Django 3.1 on 2020-09-21 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('contatos', models.ManyToManyField(related_name='_perfil_contatos_+', to='network.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=140)),
                ('data_hora_postagem', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagem', to='network.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=40)),
                ('senha', models.CharField(max_length=40)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_reacao', models.DateTimeField(auto_now_add=True)),
                ('peso', models.IntegerField(default=1)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacao', to='network.perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacao', to='network.postagem')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacao', to='network.tiporeacao')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='network.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=60)),
                ('data_hora_comentario', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='network.perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='network.postagem')),
            ],
        ),
    ]
