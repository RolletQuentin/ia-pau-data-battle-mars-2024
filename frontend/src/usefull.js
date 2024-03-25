export const bigNumber2String = (number) => {
  // Convertit le nombre en une chaîne
  let numString = number.toString();

  // Sépare la partie entière de la partie décimale
  let parts = numString.split(".");

  // Formate la partie entière avec des espaces pour les milliers
  let integerPart = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");

  // Renvoie la partie entière avec la partie décimale s'il y en a une
  return integerPart;
};
