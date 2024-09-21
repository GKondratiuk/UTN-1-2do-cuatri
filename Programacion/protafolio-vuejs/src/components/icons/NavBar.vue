<script setup>
import { ref } from 'vue';
const navegacion = ref([
  {id:1, nombre:"Educacion",enlace:"#eduacion"},
  {id:2, nombre:"Experiencia",enlace:"#Experiencia"},
  {id:3, nombre:"Proyectos",enlace:"#Proyectos"},
  {id:4, nombre:"Habilidades",enlace:"#Habilidades"},
])
</script>

<template>
<nav>
    <ul>
    <li>Educación</li>
    <li>Experiencia</li>
    <li>Proyectos</li>
    <li>Habilidades</li>
  </ul>
  </nav>
</template>


<style scoped>
ul{
    display: flex;
    gap: 2rem;
    justify-content: end;
    padding-right: 2rem;
    background-color: brown;
}
</style>