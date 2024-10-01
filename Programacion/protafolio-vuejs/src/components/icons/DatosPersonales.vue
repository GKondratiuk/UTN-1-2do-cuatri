<script setup>
const title = "Guillermo Kondratiuk";
const descripcion = "Técnico Universitario en Programación";
const residencia = "Lanus,Buenos Aires, Argentina";
const presentacion = "Bienvenido a mi portafolio, soy estudiante de la tecnicatura en programación en la Universidad Tecnológica Nacional de la Regional de San rafael Mendoza. A continuación les dejo mi contacto, mis redes, mi experiencia y trabajos realizados. Saludos";
const redesSociales = [
    {id: 1, name: 'linkedin',src: '/src/assets/linkedin.svg', url: 'https://www.linkedin.com'},
    {id: 2, name: 'github',src: '/src/assets/github.svg', url: 'https://www.github.com'},
];
</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{ title }}</h1>
            <h2>{{ descripcion }}</h2>
            <p>{{ presentacion }}</p>
            <h3>{{residencia}}</h3>
            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
                </li>
            </ul>
        </div>

    </section>
</template>

<style scoped>
section{
    display: flex;
    justify-content: center;
}
section div{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 2vh;
    padding: 20px;
    width: 80%;
    background-color: rgb(52, 51, 51);
    border-radius: 30px;
}
.container-lista{
    display: flex;
    gap: 2rem;
    margin-top: 3vh;
}

@media(max-width: 768px){
  .container-lista{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: small;
  }
}

</style>