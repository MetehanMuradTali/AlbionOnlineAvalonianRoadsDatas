import json


class Zones:
    def __init__(self):
        self.Zones = []
        self.definizeZones()
        out_file = open("dump.json", "w")
        json.dump(self.Zones, out_file)

    def addZone(self, Zone):
        self.Zones.append(Zone)

    def definizeZones(self):
        for s in range(len(cluster)):
            if cluster[s]["@id"].find("TNL") != -1:
                List = list(cluster[s]["minimapmarkers"].values())
                chests = []
                for i in range(len(List[0])):
                    lEleman = List[0][i].get("@type")
                    if (
                            lEleman == "roads_of_avalon_raid_pve" or lEleman == "roads_of_avalon_solo_pve" or lEleman == "roads_of_avalon_group_pve"):
                        chests.append(lEleman)

                nested_dict = {"@id": cluster[s]["@id"],
                                                   "@displayname": cluster[s]["@displayname"],
                                                   "@type": cluster[s]["@type"],
                                                   "resource": cluster[s]["distribution"].get("resource"),
                                                   "mobcounts": cluster[s]["mobcounts"],
                                                   "chests": chests
                                                   }
                self.addZone(nested_dict)


with open("world.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

world = jsonObject["world"]
clusters = world["clusters"]
cluster = clusters["cluster"]
zones = Zones()
