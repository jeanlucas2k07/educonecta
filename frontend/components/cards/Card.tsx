import React from "react";
import { View, Text, StyleSheet, ImageBackground, ImageSourcePropType } from "react-native";
import { LinearGradient } from "expo-linear-gradient";

// Interface das props
interface CardProps {
  title: string;
  text: string;
  image?: ImageSourcePropType; // tipo certo para imagem local ou uri
}

const Card = ({ title, text, image }: CardProps) => {
  if (image) {
    // Se existe imagem: renderiza como fundo
    return (
      <ImageBackground source={image} style={styles.card} imageStyle={styles.image}>
        <LinearGradient
          colors={["rgba(0,0,0,0.6)", "transparent"]}
          start={{ x: 0, y: 1 }}
          end={{ x: 0, y: 0.5 }}
          style={StyleSheet.absoluteFill}
        />
        <Text style={styles.title}>{title}</Text>
        <Text style={styles.text}>{text}</Text>
      </ImageBackground>
    );
  }

  // Se não existe imagem: fundo cinza
  return (
    <View style={[styles.card, { backgroundColor: '#777' }]}>
      <LinearGradient
        colors={["rgba(0,0,0,0.6)", "transparent"]}
        start={{ x: 0, y: 1 }}
        end={{ x: 0, y: 0.5 }}
        style={StyleSheet.absoluteFill}
      />
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.text}>{text}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    height: 250,
    width: 150,
    borderRadius: 12,
    overflow: 'hidden', // importante pra imagem e gradient ficarem dentro das bordas arredondadas
    justifyContent: 'flex-end', // colocar textos na parte inferior
    padding: 10,
  },
  image: {
    resizeMode: "cover",
  },
  title: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  text: {
    color: '#fff',
    fontSize: 12,
  },
});

export default Card;
