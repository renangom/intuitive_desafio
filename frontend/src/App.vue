<template>
  <div>
    <BarraNavegacao />
    <ContEudo />
  </div>
</template>

<script>
import BarraNavegacao from '@/components/Navbar/BarraNavegacao.vue'
import ContEudo from './components/Container/ContEudo.vue'
export default {
  name: 'App',
  components: {
    BarraNavegacao,
    ContEudo
}
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
  body{ 
    background: #E5E5E5;
  }
</style>
