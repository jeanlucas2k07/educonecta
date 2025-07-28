import { ScrollView, SafeAreaView, View, Text, Image, Alert, StyleSheet, TouchableOpacity } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import React, { useState, useEffect } from "react";
import Header from "@/components/header/Header";
import api from "@/src/sevices/Api";
import { useLocalSearchParams } from "expo-router";
import Button from "@/components/buttons/Button";
import Card from "@/components/cards/Card";

interface InstituicaoProps {
  id: number;
  nome: string;
  tipo: string;
  responsavel: string;
  image: string;
  descricao: string;
  cod_identificador: string;
  endereco: string
}

const Instituicao = () => {
  const params = useLocalSearchParams();
  const [instituicao, setInstituicao] = useState<InstituicaoProps | null>(null);

  async function getInstituicao() {
    try {
      const response = await api.get(`/instituicoes/${params.id}`);
      setInstituicao(response.data.insituição[0]); // conferindo nome certo do campo
    } catch (error) {
      Alert.alert("Erro ao buscar instituição", `${error}`);
    }
  }

  useEffect(() => {
    getInstituicao();
  }, []);

  return (
    <SafeAreaProvider>
        <Header />

      <SafeAreaView style={styles.container}>
        <ScrollView
         showsVerticalScrollIndicator={false}
        
        >
          {instituicao && (
            <View>
              <Image 
                source={{ uri: instituicao.image }} 
                style={styles.image} 
              />

            <Text style={styles.escolaNome}>{instituicao.nome}</Text>

              <View style={styles.textContainer}>
                <Text><Text style={styles.nomezinho}>Tipo: </Text>{instituicao.tipo}</Text>
                <Text><Text style={styles.nomezinho}> {instituicao.tipo === "Escola" ? "N° INEP: " : "CNPJ: "}</Text>{instituicao.cod_identificador}</Text>
                <Text><Text style={styles.nomezinho}>Adiministrador(a): </Text>{instituicao.responsavel}</Text>
                <Text><Text style={styles.nomezinho}>Endereco: </Text>{instituicao.endereco}</Text>
                <Text>Descrição:</Text>
                <TouchableOpacity>
                    <Text style={styles.description}>{instituicao.descricao}</Text>
                </TouchableOpacity>
              </View>

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

            <Button onPress={() => (console.log("Doar"))} text={`Doar para ${instituicao.nome}`} style={styles.button} textStyle={styles.textStyle}/>
              
            </View>
          )}
        </ScrollView>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 15,
    paddingBlockEnd: 50,
    backgroundColor: "#fff"
  },
  image: {
    width: "100%",
    height: 200,
    marginBlockEnd: 16,
    borderRadius: 5,
    elevation:3
  },
  escolaNome: {
    fontSize: 20,
    color: "black",
    fontWeight: "600"
  },
  nomezinho: {
    color: "#666"
  },
  description: {
    backgroundColor: "#f0f0f0",
    color: "#333",
    height: 80,
    borderRadius: 5,
    paddingInline: 10,
    paddingBlockStart: 20
  },
  textContainer: {
    gap: 5
  },
      button: {
      backgroundColor: "#005E1C",
      width: "100%",
      height: 50,
      borderRadius: 5,
      justifyContent: "center",
      alignItems: "center",
      elevation: 5,
      shadowColor: "#000000ff" 
    },

    textStyle: {
      color: "white",
      fontWeight: "600",
      fontSize: 16
    },
    row: {
    gap: 5,
    marginBlock: 16,
  }
});

export default Instituicao;
