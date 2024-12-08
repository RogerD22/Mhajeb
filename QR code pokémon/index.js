// import QRCode from 'https://cdn.jsdelivr.net/npm/qrcode';

// Fonction pour récupérer un Pokémon au hasard parmi les 151 premiers
async function getRandomPokemon() {
  const apiUrl = "https://pokeapi.co/api/v2/pokemon?limit=151";

  try {
    // Récupérer les Pokémons
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`Erreur: ${response.status}`);
    }
    const data = await response.json();
    const pokemonList = data.results;

    // Choisir un Pokémon au hasard
    const randomIndex = Math.floor(Math.random() * pokemonList.length);
    const randomPokemon = pokemonList[randomIndex];

    // Récupérer les détails du Pokémon choisi
    const pokemonResponse = await fetch(randomPokemon.url);
    const pokemonData = await pokemonResponse.json();

    // Récupérer le nom et le type du Pokémon
    const pokemonInfo = {
      name: pokemonData.name,
      types: pokemonData.types.map(type => type.type.name),
      image: pokemonData.sprites.front_default
    };

    return pokemonInfo;
    
  } catch (error) {
    console.error("Erreur lors de la récupération du Pokémon :", error);
  }
}


const type2cause = new Map();
type2cause.set("fire", "https://wwf.panda.org/discover/our_focus/forests_practice/forest_publications_news_and_reports/fires_forests/");
type2cause.set("water", "https://oceanconservancy.org/");
type2cause.set("grass", "https://www.ran.org/")
type2cause.set("ice", "https://www.arcticwildlife.org/")
type2cause.set("fighting", "https://www.humanesociety.org/")
type2cause.set("poison", "https://www.edf.org/")
type2cause.set("ground", "https://www.nwf.org/")
type2cause.set("vol", "https://www.audubon.org/")
type2cause.set("psy", "https://www.peta.org/")
type2cause.set("bug", "https://xerces.org/")
type2cause.set("rock", "https://www.mountainconservation.org/")
type2cause.set("ghost", "https://www.animaljusticeproject.com/")
type2cause.set("dragon", "https://www.worldwildlife.org/species")
type2cause.set("dark", "https://www.bornfree.org.uk/")
type2cause.set("steel", "https://www.wcs.org/")
type2cause.set("fairy", "https://www.fauna-flora.org/")


function generateQRCode(url) {
  // Construire l'URL de l'API avec les données de l'utilisateur
  const apiUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${encodeURIComponent(url)}`;

  // Sélectionner l'image où afficher le QR code
  const qrCodeImage = document.getElementById("qrCodeImage");

  // Modifier l'attribut `src` de l'image pour afficher le QR Code
  qrCodeImage.src = apiUrl;
  qrCodeImage.alt = `QR Code pour : ${url}`;
}


    // Fonction pour ajouter une image au centre du QR Code
    function addImageToQRCode(imageSource) {
      const pokemonImage = document.getElementById("pokemonImage");

      pokemonImage.src = imageSource;
      pokemonImage.alt = "pokémon";
    }


async function handleButtonClick(){
    const pokemon = await getRandomPokemon();
    console.log(pokemon);
    const cause = type2cause.get(pokemon.types[0]);
    console.log(cause);
    generateQRCode(cause);
    addImageToQRCode(pokemon.image);
}