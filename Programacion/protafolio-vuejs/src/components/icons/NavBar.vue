<script setup>
import { ref } from 'vue';
const navegacion = ref([
  {id:1, nombre:"Educacion",enlace:"#eduacion"},
  {id:2, nombre:"Experiencia",enlace:"#Experiencia"},
  {id:3, nombre:"Proyectos",enlace:"#Proyectos"},
  {id:4, nombre:"Habilidades",enlace:"#Habilidades"}
]);
</script>

<template>
  <nav>
      <ul>
        <!--V-for recorre el arreglo, se utiliza con una key llamada b-bind, que vincula atributos entre html y js -->
        <a v-for="nav in navegacion" :key="nav.nombre" href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
    </ul>
    </nav>
  </template>


<style scoped>
ul{
    display: flex;
    gap: 2rem;
    justify-content: end;
    align-items: center;
    padding-right: 2rem;
    height: 5vh;
    background-color: brown;
}
.nav-item{
  text-decoration: none;
}
</style>