import { View, SafeAreaView, StyleSheet, ScrollView, Text, TextInput } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { LinearGradient } from "expo-linear-gradient"
import React, { useState, useEffect } from "react";
import Header from "@/components/header/Header";
import Card from "@/components/cards/Card";
import api from "@/src/sevices/Api";

interface Instituicao {
  id: number;
  nome: string;
  tipo: string;
  // se quiser, pode adicionar outros campos que vierem no JSON, tipo cod_identificador etc.
}

const HomePage = () => {
  const [instituicoes, setInstituicoes] = useState<Instituicao[]>([])

  async function getInstituicoes() {
    try {
      const response = await api.get("/instituicoes")
      setInstituicoes(response.data.insituições)
    } catch (error) {
      console.log("error:", error)
    }
  };

  useEffect(() => {
    getInstituicoes();
  }, []);

  return (
    <SafeAreaProvider>
        <Header/>
        <SafeAreaView style={styles.container}>
          <LinearGradient
          // Background Linear Gradient
          colors={['#1E7200', '#81FA54']}
          start={{ x: 0, y: 0 }}
            end={{ x: 0, y: 1 }}
          style={StyleSheet.absoluteFill}
        />

        <TextInput style={styles.searchBar} placeholder="Pesquise uma escola, ong ou trabalho social"></TextInput>
        

        <View style={styles.scrollContainer}>
            <Text style={{color: "#ffff", fontWeight: "600", fontSize: 16, elevation: 3}}>Nossas Vitórias:</Text>
            <ScrollView
                horizontal
                showsHorizontalScrollIndicator={false}
                contentContainerStyle={styles.row}
            >
                <Card title="Card 1" text="Descrição 1" />
                <Card title="Card 2" text="Descrição 2" />
                <Card title="Card 3" text="Descrição 3" />
                <Card title="Card 4" text="Descrição 4" />
                <Card title="Card 5" text="Descrição 5" />
            </ScrollView>

        </View>

        <View>
            <Text style={{color: "#ffff", fontWeight: "600", fontSize: 16, elevation: 3}}>Instituiçoes Cadastradas:</Text>
            <ScrollView>
              {instituicoes.map((item) => (
                <View key={item.id} style={{ padding: 10, backgroundColor: 'white', marginVertical: 5, borderRadius: 5 }}>
                  <Text>Nome: {item.nome}</Text>
                  <Text>Tipo: {item.tipo}</Text>
                </View>
              ))}
            </ScrollView>
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 15,
    paddingVertical: 50,
    backgroundColor: "#007C25"
  },
  scrollContainer: {
    position: 'relative',
    marginBottom: 50
  },
  searchBar: {
    paddingHorizontal: 15,
    marginBlockEnd:50,
    backgroundColor: 'white',
    elevation: 5,
    borderRadius: 5,
  },
  row: {
    gap: 5,
    marginBlock: 16
  }
});

export default HomePage;
