<template>
  <div>
    <BarraNavegacao />
    <Container />
  </div>
</template>

<script>
import BarraNavegacao from '@/components/Navbar/BarraNavegacao.vue'
import Container from './components/Container/Container.vue'
export default {
  name: 'App',
  components: {
    BarraNavegacao,
    Container
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
