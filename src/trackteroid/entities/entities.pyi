
import typing
from .base import Entity
from ..query import Query

class ApiKey:
    prefix: str = str() 
    identifier: str = str() 
    id: str = str() 
    resource_id: str = str() 



class Appointment(Entity):
    resource: Resource = Resource 
    resource_id: str = str() 
    context_id: str = str() 
    context: Context = Context 
    type: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Appointment:... 
    def by_id(self, target, *ids) -> Query(Appointment):... 
    def by_metadata(self, target, *dictionaries) -> Query(Appointment):... 
    def create(self) -> Appointment:... 
    def create_batch(self, *attributes) -> Appointment:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Appointment:... 
    def get_all(self, projections=None) -> Appointment:... 
    def get_first(self, projections=None) -> Appointment:... 
    def get_inputs(self, projections=None) -> Appointment:... 
    def get_one(self, projections=None) -> Appointment:... 
    def get_outputs(self, projections=None) -> Appointment:... 
    def inject(self, filter) -> Query(Appointment):... 
    def not_by_id(self, target, *ids) -> Query(Appointment):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Appointment):... 


class Asset(Entity):
    ancestors: TypedContext = TypedContext 
    name: str = str() 
    parent: Context = Context 
    type_id: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    context_id: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    versions: AssetVersion = AssetVersion 
    latest_version: AssetVersion = AssetVersion 
    project_id: str = str() 
    type: AssetType = AssetType 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Asset:... 
    def by_id(self, target, *ids) -> Query(Asset):... 
    def by_metadata(self, target, *dictionaries) -> Query(Asset):... 
    def by_name(self, target, *names) -> Query(Asset):... 
    def by_type(self, target, *types) -> Query(Asset):... 
    def create(self, name, type) -> Asset:... 
    def create_batch(self, *attributes) -> Asset:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Asset:... 
    def get_all(self, projections=None) -> Asset:... 
    def get_first(self, projections=None) -> Asset:... 
    def get_inputs(self, projections=None) -> Asset:... 
    def get_one(self, projections=None) -> Asset:... 
    def get_outputs(self, projections=None) -> Asset:... 
    def inject(self, filter) -> Query(Asset):... 
    def not_by_id(self, target, *ids) -> Query(Asset):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Asset):... 
    def not_by_name(self, target, *names) -> Query(Asset):... 
    def not_by_type(self, target, *types) -> Query(Asset):... 


class AssetBuild(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetBuild:... 
    def by_assignee(self, target, *assignees) -> Query(AssetBuild):... 
    def by_id(self, target, *ids) -> Query(AssetBuild):... 
    def by_incoming_link(self, target, *ids) -> Query(AssetBuild):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(AssetBuild):... 
    def by_metadata(self, target, *dictionaries) -> Query(AssetBuild):... 
    def by_name(self, target, *names) -> Query(AssetBuild):... 
    def by_outgoing_link(self, target, *ids) -> Query(AssetBuild):... 
    def by_state(self, target, *states) -> Query(AssetBuild):... 
    def by_status(self, target, *statuses) -> Query(AssetBuild):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(AssetBuild):... 
    def by_type(self, target, *types) -> Query(AssetBuild):... 
    def create(self) -> AssetBuild:... 
    def create_batch(self, *attributes) -> AssetBuild:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> AssetBuild:... 
    def get_all(self, projections=None) -> AssetBuild:... 
    def get_first(self, projections=None) -> AssetBuild:... 
    def get_inputs(self, projections=None) -> AssetBuild:... 
    def get_one(self, projections=None) -> AssetBuild:... 
    def get_outputs(self, projections=None) -> AssetBuild:... 
    def inject(self, filter) -> Query(AssetBuild):... 
    def link_inputs(self, entity_collection) -> AssetBuild:... 
    def link_outputs(self, entity_collection) -> AssetBuild:... 
    def not_by_assignee(self, target, *assignees) -> Query(AssetBuild):... 
    def not_by_id(self, target, *ids) -> Query(AssetBuild):... 
    def not_by_incoming_link(self, target, *ids) -> Query(AssetBuild):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(AssetBuild):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(AssetBuild):... 
    def not_by_name(self, target, *names) -> Query(AssetBuild):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(AssetBuild):... 
    def not_by_state(self, target, *states) -> Query(AssetBuild):... 
    def not_by_status(self, target, *statuses) -> Query(AssetBuild):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(AssetBuild):... 
    def not_by_type(self, target, *types) -> Query(AssetBuild):... 
    def unlink_inputs(self, entity_collection) -> AssetBuild:... 
    def unlink_outputs(self, entity_collection) -> AssetBuild:... 


class AssetCustomAttributeLink:
    to_entity_type: str = str() 
    from_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    asset: Asset = Asset 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetCustomAttributeLink:... 


class AssetCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    from_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    asset: Asset = Asset 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetCustomAttributeLinkFrom:... 


class AssetCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetCustomAttributeValue:... 


class AssetType(Entity):
    short: str = str() 
    component: str = str() 
    assets: Asset = Asset 
    name: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetType:... 
    def by_id(self, target, *ids) -> Query(AssetType):... 
    def by_metadata(self, target, *dictionaries) -> Query(AssetType):... 
    def create(self) -> AssetType:... 
    def create_batch(self, *attributes) -> AssetType:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> AssetType:... 
    def get_all(self, projections=None) -> AssetType:... 
    def get_first(self, projections=None) -> AssetType:... 
    def get_inputs(self, projections=None) -> AssetType:... 
    def get_one(self, projections=None) -> AssetType:... 
    def get_outputs(self, projections=None) -> AssetType:... 
    def inject(self, filter) -> Query(AssetType):... 
    def not_by_id(self, target, *ids) -> Query(AssetType):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(AssetType):... 


class AssetVersion(Entity):
    comment: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: AssetVersionLink = AssetVersionLink 
    id: str = str() 
    asset_id: str = str() 
    user_id: str = str() 
    version: int = int() 
    asset: Asset = Asset 
    project_id: str = str() 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    status: Status = Status 
    components: Component = Component 
    status_id: str = str() 
    thumbnail_id: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    lists: AssetVersionList = AssetVersionList 
    uses_versions: AssetVersion = AssetVersion 
    link: str = str() 
    user: User = User 
    date: str = str() 
    used_in_versions: AssetVersion = AssetVersion 
    task: Task = Task 
    task_id: str = str() 
    review_session_objects: ReviewSessionObject = ReviewSessionObject 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    notes: Note = Note 
    thumbnail_url: object 
    is_latest_version: bool = bool() 
    outgoing_links: AssetVersionLink = AssetVersionLink 
    is_published: bool = bool() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersion:... 
    def by_id(self, target, *ids) -> Query(AssetVersion):... 
    def by_incoming_link(self, target, *ids) -> Query(AssetVersion):... 
    def by_metadata(self, target, *dictionaries) -> Query(AssetVersion):... 
    def by_name(self, target, *names) -> Query(AssetVersion):... 
    def by_outgoing_link(self, target, *ids) -> Query(AssetVersion):... 
    def by_publish_state(self, target, publish_state) -> Query(AssetVersion):... 
    def by_publish_time(self, target, start=None, end=None) -> Query(AssetVersion):... 
    def by_publisher(self, target, *publishers) -> Query(AssetVersion):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(AssetVersion):... 
    def by_state(self, target, *states) -> Query(AssetVersion):... 
    def by_status(self, target, *statuses) -> Query(AssetVersion):... 
    def by_type(self, target, *types) -> Query(AssetVersion):... 
    def by_version(self, target, *versions) -> Query(AssetVersion):... 
    def create(self, task) -> AssetVersion:... 
    def create_batch(self, *attributes) -> AssetVersion:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> AssetVersion:... 
    def get_all(self, projections=None) -> AssetVersion:... 
    def get_first(self, projections=None) -> AssetVersion:... 
    def get_inputs(self, projections=None) -> AssetVersion:... 
    def get_one(self, projections=None) -> AssetVersion:... 
    def get_outputs(self, projections=None) -> AssetVersion:... 
    def inject(self, filter) -> Query(AssetVersion):... 
    def link_inputs(self, entity_collection) -> AssetVersion:... 
    def link_outputs(self, entity_collection) -> AssetVersion:... 
    def not_by_id(self, target, *ids) -> Query(AssetVersion):... 
    def not_by_incoming_link(self, target, *ids) -> Query(AssetVersion):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(AssetVersion):... 
    def not_by_name(self, target, *names) -> Query(AssetVersion):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(AssetVersion):... 
    def not_by_publish_state(self, target, publish_state) -> Query(AssetVersion):... 
    def not_by_publish_time(self, target, start=None, end=None) -> Query(AssetVersion):... 
    def not_by_publisher(self, target, *publishers) -> Query(AssetVersion):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(AssetVersion):... 
    def not_by_state(self, target, *states) -> Query(AssetVersion):... 
    def not_by_status(self, target, *statuses) -> Query(AssetVersion):... 
    def not_by_type(self, target, *types) -> Query(AssetVersion):... 
    def not_by_version(self, target, *versions) -> Query(AssetVersion):... 
    def unlink_inputs(self, entity_collection) -> AssetVersion:... 
    def unlink_outputs(self, entity_collection) -> AssetVersion:... 


class AssetVersionCustomAttributeLink:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    asset_version: AssetVersion = AssetVersion 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionCustomAttributeLink:... 


class AssetVersionCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    asset_version: AssetVersion = AssetVersion 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionCustomAttributeLinkFrom:... 


class AssetVersionCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionCustomAttributeValue:... 


class AssetVersionLink(Entity):
    from: AssetVersion = AssetVersion 
    to_id: str = str() 
    to: AssetVersion = AssetVersion 
    from_id: str = str() 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionLink:... 
    def by_id(self, target, *ids) -> Query(AssetVersionLink):... 
    def by_metadata(self, target, *dictionaries) -> Query(AssetVersionLink):... 
    def create(self) -> AssetVersionLink:... 
    def create_batch(self, *attributes) -> AssetVersionLink:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> AssetVersionLink:... 
    def get_all(self, projections=None) -> AssetVersionLink:... 
    def get_first(self, projections=None) -> AssetVersionLink:... 
    def get_inputs(self, projections=None) -> AssetVersionLink:... 
    def get_one(self, projections=None) -> AssetVersionLink:... 
    def get_outputs(self, projections=None) -> AssetVersionLink:... 
    def inject(self, filter) -> Query(AssetVersionLink):... 
    def not_by_id(self, target, *ids) -> Query(AssetVersionLink):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(AssetVersionLink):... 


class AssetVersionList(List):
    category: ListCategory = ListCategory 
    project_id: str = str() 
    user_id: str = str() 
    name: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    items: AssetVersion = AssetVersion 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    project: Project = Project 
    owner: User = User 
    is_open: bool = bool() 
    system_type: str = str() 
    date: str = str() 
    category_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionList:... 
    def by_id(self, target, *ids) -> Query(AssetVersionList):... 
    def by_metadata(self, target, *dictionaries) -> Query(AssetVersionList):... 
    def by_name(self, target, *names) -> Query(AssetVersionList):... 
    def create(self, task) -> AssetVersionList:... 
    def create_batch(self, *attributes) -> AssetVersionList:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> AssetVersionList:... 
    def get_all(self, projections=None) -> AssetVersionList:... 
    def get_first(self, projections=None) -> AssetVersionList:... 
    def get_inputs(self, projections=None) -> AssetVersionList:... 
    def get_one(self, projections=None) -> AssetVersionList:... 
    def get_outputs(self, projections=None) -> AssetVersionList:... 
    def inject(self, filter) -> Query(AssetVersionList):... 
    def not_by_id(self, target, *ids) -> Query(AssetVersionList):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(AssetVersionList):... 
    def not_by_name(self, target, *names) -> Query(AssetVersionList):... 


class AssetVersionStatusChange:
    status: Status = Status 
    user_id: str = str() 
    parent: AssetVersion = AssetVersion 
    status_id: str = str() 
    parent_type: str = str() 
    parent_id: str = str() 
    user: User = User 
    from_status: Status = Status 
    date: str = str() 
    from_status_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> AssetVersionStatusChange:... 


class AssetVersionStatusRuleGroup:
    status: Status = Status 
    status_rules: StatusRule = StatusRule 
    status_id: str = str() 
    entity_type: str = str() 
    role_id: str = str() 
    schema_id: str = str() 
    role: SecurityRole = SecurityRole 
    id: str = str() 
    schema: ProjectSchema = ProjectSchema 



class BaseUser:
    first_name: str = str() 
    last_name: str = str() 
    dashboard_resources: DashboardResource = DashboardResource 
    thumbnail_id: str = str() 
    email: str = str() 
    id: str = str() 
    assignments: Appointment = Appointment 
    appointments: Appointment = Appointment 
    thumbnail_url: object 
    allocations: Appointment = Appointment 
    thumbnail: Component = Component 
    resource_type: str = str() 



class CalendarEvent:
    calendar_event_resources: CalendarEventResource = CalendarEventResource 
    everyone: bool = bool() 
    end: str = str() 
    name: str = str() 
    type_id: str = str() 
    leave: bool = bool() 
    created_at: str = str() 
    created_by: User = User 
    forecast: bool = bool() 
    project: Project = Project 
    start: str = str() 
    effort: float = float() 
    created_by_id: str = str() 
    estimate: float = float() 
    project_id: str = str() 
    type: Type = Type 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CalendarEvent:... 


class CalendarEventResource:
    resource: Resource = Resource 
    resource_id: str = str() 
    calendar_event_id: str = str() 
    created_at: str = str() 
    created_by: User = User 
    calendar_event: CalendarEvent = CalendarEvent 
    created_by_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CalendarEventResource:... 


class Collaborator:
    created_from_shared_url: str = str() 
    first_name: str = str() 
    last_name: str = str() 
    assignments: Appointment = Appointment 
    thumbnail_id: str = str() 
    thumbnail: Component = Component 
    id: str = str() 
    dashboard_resources: DashboardResource = DashboardResource 
    appointments: Appointment = Appointment 
    thumbnail_url: object 
    allocations: Appointment = Appointment 
    email: str = str() 
    resource_type: str = str() 



class Component(Entity):
    container: ContainerComponent = ContainerComponent 
    name: str = str() 
    component_locations: ComponentLocation = ComponentLocation 
    file_type: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    container_id: str = str() 
    version_id: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    version: AssetVersion = AssetVersion 
    system_type: str = str() 
    size: int = int() 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Component:... 
    def by_file_type(self, target, *file_types) -> Query(Component):... 
    def by_id(self, target, *ids) -> Query(Component):... 
    def by_location(self, target, *component_locations) -> Query(Component):... 
    def by_metadata(self, target, *dictionaries) -> Query(Component):... 
    def by_name(self, target, *names) -> Query(Component):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(Component):... 
    def by_size(self, target, minimum=0, maximum=0) -> Query(Component):... 
    def by_system_type(self, target, *system_types) -> Query(Component):... 
    def by_version(self, target, *versions) -> Query(Component):... 
    def create(self) -> Component:... 
    def create_batch(self, *attributes) -> Component:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Component:... 
    def get_all(self, projections=None) -> Component:... 
    def get_first(self, projections=None) -> Component:... 
    def get_inputs(self, projections=None) -> Component:... 
    def get_one(self, projections=None) -> Component:... 
    def get_outputs(self, projections=None) -> Component:... 
    def inject(self, filter) -> Query(Component):... 
    def not_by_file_type(self, target, *file_types) -> Query(Component):... 
    def not_by_id(self, target, *ids) -> Query(Component):... 
    def not_by_location(self, target, *component_locations) -> Query(Component):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Component):... 
    def not_by_name(self, target, *names) -> Query(Component):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(Component):... 
    def not_by_size(self, target, minimum=0, maximum=0) -> Query(Component):... 
    def not_by_system_type(self, target, *system_types) -> Query(Component):... 
    def not_by_version(self, target, *versions) -> Query(Component):... 


class ComponentCustomAttributeLink:
    to_entity_type: str = str() 
    component: Component = Component 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ComponentCustomAttributeLink:... 


class ComponentCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    component: Component = Component 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ComponentCustomAttributeLinkFrom:... 


class ComponentLocation(Entity):
    component_id: str = str() 
    url: object 
    component: Component = Component 
    resource_identifier: str = str() 
    location: Location = Location 
    location_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ComponentLocation:... 
    def by_id(self, target, *ids) -> Query(ComponentLocation):... 
    def by_metadata(self, target, *dictionaries) -> Query(ComponentLocation):... 
    def by_name(self, target, *names) -> Query(ComponentLocation):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(ComponentLocation):... 
    def by_version(self, target, *versions) -> Query(ComponentLocation):... 
    def create(self) -> ComponentLocation:... 
    def create_batch(self, *attributes) -> ComponentLocation:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ComponentLocation:... 
    def get_all(self, projections=None) -> ComponentLocation:... 
    def get_first(self, projections=None) -> ComponentLocation:... 
    def get_inputs(self, projections=None) -> ComponentLocation:... 
    def get_one(self, projections=None) -> ComponentLocation:... 
    def get_outputs(self, projections=None) -> ComponentLocation:... 
    def inject(self, filter) -> Query(ComponentLocation):... 
    def not_by_id(self, target, *ids) -> Query(ComponentLocation):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ComponentLocation):... 
    def not_by_name(self, target, *names) -> Query(ComponentLocation):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(ComponentLocation):... 
    def not_by_version(self, target, *versions) -> Query(ComponentLocation):... 


class ContainerComponent(Component):
    container: ContainerComponent = ContainerComponent 
    name: str = str() 
    component_locations: ComponentLocation = ComponentLocation 
    file_type: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    container_id: str = str() 
    version_id: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    version: AssetVersion = AssetVersion 
    system_type: str = str() 
    members: Component = Component 
    metadata: typing.List = [Metadata] 
    id: str = str() 
    size: int = int() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ContainerComponent:... 
    def by_file_type(self, target, *file_types) -> Query(ContainerComponent):... 
    def by_id(self, target, *ids) -> Query(ContainerComponent):... 
    def by_location(self, target, *component_locations) -> Query(ContainerComponent):... 
    def by_metadata(self, target, *dictionaries) -> Query(ContainerComponent):... 
    def by_name(self, target, *names) -> Query(ContainerComponent):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(ContainerComponent):... 
    def by_size(self, target, minimum=0, maximum=0) -> Query(ContainerComponent):... 
    def by_system_type(self, target, *system_types) -> Query(ContainerComponent):... 
    def by_version(self, target, *versions) -> Query(ContainerComponent):... 
    def create(self) -> ContainerComponent:... 
    def create_batch(self, *attributes) -> ContainerComponent:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ContainerComponent:... 
    def get_all(self, projections=None) -> ContainerComponent:... 
    def get_first(self, projections=None) -> ContainerComponent:... 
    def get_inputs(self, projections=None) -> ContainerComponent:... 
    def get_one(self, projections=None) -> ContainerComponent:... 
    def get_outputs(self, projections=None) -> ContainerComponent:... 
    def inject(self, filter) -> Query(ContainerComponent):... 
    def not_by_file_type(self, target, *file_types) -> Query(ContainerComponent):... 
    def not_by_id(self, target, *ids) -> Query(ContainerComponent):... 
    def not_by_location(self, target, *component_locations) -> Query(ContainerComponent):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ContainerComponent):... 
    def not_by_name(self, target, *names) -> Query(ContainerComponent):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(ContainerComponent):... 
    def not_by_size(self, target, minimum=0, maximum=0) -> Query(ContainerComponent):... 
    def not_by_system_type(self, target, *system_types) -> Query(ContainerComponent):... 
    def not_by_version(self, target, *versions) -> Query(ContainerComponent):... 


class Context(Entity):
    created_at: str = str() 
    managers: Manager = Manager 
    created_by: User = User 
    id: str = str() 
    timelogs: Timelog = Timelog 
    _link: str = str() 
    children: Context = Context 
    parent_id: str = str() 
    project_id: str = str() 
    thumbnail: Component = Component 
    scopes: Scope = Scope 
    parent: Context = Context 
    thumbnail_id: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    appointments: Appointment = Appointment 
    link: str = str() 
    name: str = str() 
    assets: Asset = Asset 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    notes: Note = Note 
    assignments: Appointment = Appointment 
    thumbnail_url: object 
    allocations: Appointment = Appointment 
    created_by_id: str = str() 
    context_type: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Context:... 
    def by_id(self, target, *ids) -> Query(Context):... 
    def by_metadata(self, target, *dictionaries) -> Query(Context):... 
    def create(self) -> Context:... 
    def create_batch(self, *attributes) -> Context:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Context:... 
    def get_all(self, projections=None) -> Context:... 
    def get_first(self, projections=None) -> Context:... 
    def get_inputs(self, projections=None) -> Context:... 
    def get_one(self, projections=None) -> Context:... 
    def get_outputs(self, projections=None) -> Context:... 
    def inject(self, filter) -> Query(Context):... 
    def not_by_id(self, target, *ids) -> Query(Context):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Context):... 


class ContextCustomAttributeLink:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    context: Context = Context 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ContextCustomAttributeLink:... 


class ContextCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    context: Context = Context 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ContextCustomAttributeLinkFrom:... 


class ContextCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ContextCustomAttributeValue:... 


class CustomAttributeConfiguration:
    sort: int = int() 
    core: bool = bool() 
    group_id: str = str() 
    group: CustomAttributeGroup = CustomAttributeGroup 
    key: str = str() 
    type_id: str = str() 
    default: typing.Any = None 
    type: CustomAttributeType = CustomAttributeType 
    object_type: ObjectType = ObjectType 
    label: str = str() 
    read_security_roles: SecurityRole = SecurityRole 
    entity_type: str = str() 
    values: CustomAttributeValue = CustomAttributeValue 
    object_type_id: str = str() 
    write_security_roles: SecurityRole = SecurityRole 
    is_hierarchical: bool = bool() 
    project_id: str = str() 
    config: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeConfiguration:... 


class CustomAttributeGroup:
    custom_attribute_configurations: CustomAttributeConfiguration = CustomAttributeConfiguration 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeGroup:... 


class CustomAttributeLink:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeLink:... 


class CustomAttributeLinkConfiguration:
    sort: int = int() 
    core: bool = bool() 
    group_id: str = str() 
    group: CustomAttributeGroup = CustomAttributeGroup 
    key: str = str() 
    one_to_one: bool = bool() 
    object_type: ObjectType = ObjectType 
    object_type_id_to: str = str() 
    entity_type_to: str = str() 
    label: str = str() 
    read_security_roles: SecurityRole = SecurityRole 
    entity_type: str = str() 
    object_type_id: str = str() 
    write_security_roles: SecurityRole = SecurityRole 
    object_type_to: ObjectType = ObjectType 
    project_id: str = str() 
    config: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeLinkConfiguration:... 


class CustomAttributeLinkFrom:
    to_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeLinkFrom:... 


class CustomAttributeType:
    form_config: str = str() 
    core: bool = bool() 
    id: str = str() 
    name: str = str() 
    custom_attribute_configurations: CustomAttributeConfiguration = CustomAttributeConfiguration 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeType:... 


class CustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomAttributeValue:... 


class CustomConfigurationBase:
    sort: int = int() 
    core: bool = bool() 
    group_id: str = str() 
    group: CustomAttributeGroup = CustomAttributeGroup 
    object_type_id: str = str() 
    entity_type: str = str() 
    object_type: ObjectType = ObjectType 
    label: str = str() 
    read_security_roles: SecurityRole = SecurityRole 
    key: str = str() 
    write_security_roles: SecurityRole = SecurityRole 
    project_id: str = str() 
    config: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> CustomConfigurationBase:... 


class Dashboard:
    name: str = str() 
    created_by: User = User 
    dashboard_resources: DashboardResource = DashboardResource 
    widgets: DashboardWidget = DashboardWidget 
    created_by_id: str = str() 
    is_shared_with_everyone: bool = bool() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Dashboard:... 


class DashboardResource:
    dashboard_id: str = str() 
    resource: Resource = Resource 
    dashboard: Dashboard = Dashboard 
    resource_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> DashboardResource:... 


class DashboardWidget:
    sort: float = float() 
    type: str = str() 
    dashboard_id: str = str() 
    dashboard: Dashboard = Dashboard 
    config: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> DashboardWidget:... 


class Disk:
    windows: str = str() 
    unix: str = str() 
    id: str = str() 
    projects: Project = Project 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Disk:... 


class EntitySetting(Entity):
    parent_id: str = str() 
    parent_type: str = str() 
    name: str = str() 
    value: str = str() 
    group: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> EntitySetting:... 
    def by_id(self, target, *ids) -> Query(EntitySetting):... 
    def by_metadata(self, target, *dictionaries) -> Query(EntitySetting):... 
    def create(self) -> EntitySetting:... 
    def create_batch(self, *attributes) -> EntitySetting:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> EntitySetting:... 
    def get_all(self, projections=None) -> EntitySetting:... 
    def get_first(self, projections=None) -> EntitySetting:... 
    def get_inputs(self, projections=None) -> EntitySetting:... 
    def get_one(self, projections=None) -> EntitySetting:... 
    def get_outputs(self, projections=None) -> EntitySetting:... 
    def inject(self, filter) -> Query(EntitySetting):... 
    def not_by_id(self, target, *ids) -> Query(EntitySetting):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(EntitySetting):... 


class Episode(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Episode:... 
    def by_assignee(self, target, *assignees) -> Query(Episode):... 
    def by_id(self, target, *ids) -> Query(Episode):... 
    def by_incoming_link(self, target, *ids) -> Query(Episode):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Episode):... 
    def by_metadata(self, target, *dictionaries) -> Query(Episode):... 
    def by_name(self, target, *names) -> Query(Episode):... 
    def by_outgoing_link(self, target, *ids) -> Query(Episode):... 
    def by_state(self, target, *states) -> Query(Episode):... 
    def by_status(self, target, *statuses) -> Query(Episode):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Episode):... 
    def by_type(self, target, *types) -> Query(Episode):... 
    def create(self) -> Episode:... 
    def create_batch(self, *attributes) -> Episode:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Episode:... 
    def get_all(self, projections=None) -> Episode:... 
    def get_first(self, projections=None) -> Episode:... 
    def get_inputs(self, projections=None) -> Episode:... 
    def get_one(self, projections=None) -> Episode:... 
    def get_outputs(self, projections=None) -> Episode:... 
    def inject(self, filter) -> Query(Episode):... 
    def link_inputs(self, entity_collection) -> Episode:... 
    def link_outputs(self, entity_collection) -> Episode:... 
    def not_by_assignee(self, target, *assignees) -> Query(Episode):... 
    def not_by_id(self, target, *ids) -> Query(Episode):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Episode):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Episode):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Episode):... 
    def not_by_name(self, target, *names) -> Query(Episode):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Episode):... 
    def not_by_state(self, target, *states) -> Query(Episode):... 
    def not_by_status(self, target, *statuses) -> Query(Episode):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Episode):... 
    def not_by_type(self, target, *types) -> Query(Episode):... 
    def unlink_inputs(self, entity_collection) -> Episode:... 
    def unlink_outputs(self, entity_collection) -> Episode:... 


class Event(Entity):
    insert: str = str() 
    user_id: str = str() 
    created_at: str = str() 
    parent_type: str = str() 
    project: Project = Project 
    parent_id: str = str() 
    user: User = User 
    action: str = str() 
    feeds: Feed = Feed 
    project_id: str = str() 
    data: str = str() 
    id: int = int() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Event:... 
    def by_action(self, target, *actions) -> Query(Event):... 
    def by_data(self, target, *datas) -> Query(Event):... 
    def by_id(self, target, *ids) -> Query(Event):... 
    def by_metadata(self, target, *dictionaries) -> Query(Event):... 
    def by_name(self, target, *names) -> Query(Event):... 
    def create(self) -> Event:... 
    def create_batch(self, *attributes) -> Event:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Event:... 
    def get_all(self, projections=None) -> Event:... 
    def get_first(self, projections=None) -> Event:... 
    def get_inputs(self, projections=None) -> Event:... 
    def get_one(self, projections=None) -> Event:... 
    def get_outputs(self, projections=None) -> Event:... 
    def inject(self, filter) -> Query(Event):... 
    def not_by_action(self, target, *actions) -> Query(Event):... 
    def not_by_data(self, target, *datas) -> Query(Event):... 
    def not_by_id(self, target, *ids) -> Query(Event):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Event):... 
    def not_by_name(self, target, *names) -> Query(Event):... 


class Feed:
    distance: int = int() 
    created_at: str = str() 
    id: str = str() 
    relation: str = str() 
    social_id: int = int() 
    cluster_id: str = str() 
    event: Event = Event 
    owner_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Feed:... 


class FileComponent(Component):
    container: ContainerComponent = ContainerComponent 
    name: str = str() 
    component_locations: ComponentLocation = ComponentLocation 
    file_type: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    container_id: str = str() 
    version_id: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    version: AssetVersion = AssetVersion 
    system_type: str = str() 
    metadata: typing.List = [Metadata] 
    id: str = str() 
    size: int = int() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> FileComponent:... 
    def by_file_type(self, target, *file_types) -> Query(FileComponent):... 
    def by_id(self, target, *ids) -> Query(FileComponent):... 
    def by_location(self, target, *component_locations) -> Query(FileComponent):... 
    def by_metadata(self, target, *dictionaries) -> Query(FileComponent):... 
    def by_name(self, target, *names) -> Query(FileComponent):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(FileComponent):... 
    def by_size(self, target, minimum=0, maximum=0) -> Query(FileComponent):... 
    def by_system_type(self, target, *system_types) -> Query(FileComponent):... 
    def by_version(self, target, *versions) -> Query(FileComponent):... 
    def create(self) -> FileComponent:... 
    def create_batch(self, *attributes) -> FileComponent:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> FileComponent:... 
    def get_all(self, projections=None) -> FileComponent:... 
    def get_first(self, projections=None) -> FileComponent:... 
    def get_inputs(self, projections=None) -> FileComponent:... 
    def get_one(self, projections=None) -> FileComponent:... 
    def get_outputs(self, projections=None) -> FileComponent:... 
    def inject(self, filter) -> Query(FileComponent):... 
    def not_by_file_type(self, target, *file_types) -> Query(FileComponent):... 
    def not_by_id(self, target, *ids) -> Query(FileComponent):... 
    def not_by_location(self, target, *component_locations) -> Query(FileComponent):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(FileComponent):... 
    def not_by_name(self, target, *names) -> Query(FileComponent):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(FileComponent):... 
    def not_by_size(self, target, minimum=0, maximum=0) -> Query(FileComponent):... 
    def not_by_system_type(self, target, *system_types) -> Query(FileComponent):... 
    def not_by_version(self, target, *versions) -> Query(FileComponent):... 


class Folder(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Folder:... 
    def by_assignee(self, target, *assignees) -> Query(Folder):... 
    def by_id(self, target, *ids) -> Query(Folder):... 
    def by_incoming_link(self, target, *ids) -> Query(Folder):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Folder):... 
    def by_metadata(self, target, *dictionaries) -> Query(Folder):... 
    def by_name(self, target, *names) -> Query(Folder):... 
    def by_outgoing_link(self, target, *ids) -> Query(Folder):... 
    def by_state(self, target, *states) -> Query(Folder):... 
    def by_status(self, target, *statuses) -> Query(Folder):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Folder):... 
    def by_type(self, target, *types) -> Query(Folder):... 
    def create(self) -> Folder:... 
    def create_batch(self, *attributes) -> Folder:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Folder:... 
    def get_all(self, projections=None) -> Folder:... 
    def get_first(self, projections=None) -> Folder:... 
    def get_inputs(self, projections=None) -> Folder:... 
    def get_one(self, projections=None) -> Folder:... 
    def get_outputs(self, projections=None) -> Folder:... 
    def inject(self, filter) -> Query(Folder):... 
    def link_inputs(self, entity_collection) -> Folder:... 
    def link_outputs(self, entity_collection) -> Folder:... 
    def not_by_assignee(self, target, *assignees) -> Query(Folder):... 
    def not_by_id(self, target, *ids) -> Query(Folder):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Folder):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Folder):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Folder):... 
    def not_by_name(self, target, *names) -> Query(Folder):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Folder):... 
    def not_by_state(self, target, *states) -> Query(Folder):... 
    def not_by_status(self, target, *statuses) -> Query(Folder):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Folder):... 
    def not_by_type(self, target, *types) -> Query(Folder):... 
    def unlink_inputs(self, entity_collection) -> Folder:... 
    def unlink_outputs(self, entity_collection) -> Folder:... 


class Group(Entity):
    assignments: Appointment = Appointment 
    name: str = str() 
    parent: Group = Group 
    parent_id: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    children: Group = Group 
    memberships: Membership = Membership 
    dashboard_resources: DashboardResource = DashboardResource 
    appointments: Appointment = Appointment 
    link: str = str() 
    allocations: Appointment = Appointment 
    local: bool = bool() 
    id: str = str() 
    resource_type: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Group:... 
    def by_id(self, target, *ids) -> Query(Group):... 
    def by_metadata(self, target, *dictionaries) -> Query(Group):... 
    def by_name(self, target, *names) -> Query(Group):... 
    def create(self) -> Group:... 
    def create_batch(self, *attributes) -> Group:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Group:... 
    def get_all(self, projections=None) -> Group:... 
    def get_first(self, projections=None) -> Group:... 
    def get_inputs(self, projections=None) -> Group:... 
    def get_one(self, projections=None) -> Group:... 
    def get_outputs(self, projections=None) -> Group:... 
    def inject(self, filter) -> Query(Group):... 
    def not_by_id(self, target, *ids) -> Query(Group):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Group):... 
    def not_by_name(self, target, *names) -> Query(Group):... 


class GroupCustomAttributeLink:
    to_entity_type: str = str() 
    group: Group = Group 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> GroupCustomAttributeLink:... 


class GroupCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    group: Group = Group 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> GroupCustomAttributeLinkFrom:... 


class Image(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Image:... 
    def by_assignee(self, target, *assignees) -> Query(Image):... 
    def by_id(self, target, *ids) -> Query(Image):... 
    def by_incoming_link(self, target, *ids) -> Query(Image):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Image):... 
    def by_metadata(self, target, *dictionaries) -> Query(Image):... 
    def by_name(self, target, *names) -> Query(Image):... 
    def by_outgoing_link(self, target, *ids) -> Query(Image):... 
    def by_state(self, target, *states) -> Query(Image):... 
    def by_status(self, target, *statuses) -> Query(Image):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Image):... 
    def by_type(self, target, *types) -> Query(Image):... 
    def create(self) -> Image:... 
    def create_batch(self, *attributes) -> Image:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Image:... 
    def get_all(self, projections=None) -> Image:... 
    def get_first(self, projections=None) -> Image:... 
    def get_inputs(self, projections=None) -> Image:... 
    def get_one(self, projections=None) -> Image:... 
    def get_outputs(self, projections=None) -> Image:... 
    def inject(self, filter) -> Query(Image):... 
    def link_inputs(self, entity_collection) -> Image:... 
    def link_outputs(self, entity_collection) -> Image:... 
    def not_by_assignee(self, target, *assignees) -> Query(Image):... 
    def not_by_id(self, target, *ids) -> Query(Image):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Image):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Image):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Image):... 
    def not_by_name(self, target, *names) -> Query(Image):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Image):... 
    def not_by_state(self, target, *states) -> Query(Image):... 
    def not_by_status(self, target, *statuses) -> Query(Image):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Image):... 
    def not_by_type(self, target, *types) -> Query(Image):... 
    def unlink_inputs(self, entity_collection) -> Image:... 
    def unlink_outputs(self, entity_collection) -> Image:... 


class Information(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Information:... 
    def by_assignee(self, target, *assignees) -> Query(Information):... 
    def by_id(self, target, *ids) -> Query(Information):... 
    def by_incoming_link(self, target, *ids) -> Query(Information):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Information):... 
    def by_metadata(self, target, *dictionaries) -> Query(Information):... 
    def by_name(self, target, *names) -> Query(Information):... 
    def by_outgoing_link(self, target, *ids) -> Query(Information):... 
    def by_state(self, target, *states) -> Query(Information):... 
    def by_status(self, target, *statuses) -> Query(Information):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Information):... 
    def by_type(self, target, *types) -> Query(Information):... 
    def create(self) -> Information:... 
    def create_batch(self, *attributes) -> Information:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Information:... 
    def get_all(self, projections=None) -> Information:... 
    def get_first(self, projections=None) -> Information:... 
    def get_inputs(self, projections=None) -> Information:... 
    def get_one(self, projections=None) -> Information:... 
    def get_outputs(self, projections=None) -> Information:... 
    def inject(self, filter) -> Query(Information):... 
    def link_inputs(self, entity_collection) -> Information:... 
    def link_outputs(self, entity_collection) -> Information:... 
    def not_by_assignee(self, target, *assignees) -> Query(Information):... 
    def not_by_id(self, target, *ids) -> Query(Information):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Information):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Information):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Information):... 
    def not_by_name(self, target, *names) -> Query(Information):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Information):... 
    def not_by_state(self, target, *states) -> Query(Information):... 
    def not_by_status(self, target, *statuses) -> Query(Information):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Information):... 
    def not_by_type(self, target, *types) -> Query(Information):... 
    def unlink_inputs(self, entity_collection) -> Information:... 
    def unlink_outputs(self, entity_collection) -> Information:... 


class Job(Entity):
    status: str = str() 
    user_id: str = str() 
    finished_at: str = str() 
    created_at: str = str() 
    data: str = str() 
    user: User = User 
    type: str = str() 
    id: str = str() 
    job_components: JobComponent = JobComponent 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Job:... 
    def by_creation_date(self, target, creation_date) -> Query(Job):... 
    def by_data(self, target, *dictionaries) -> Query(Job):... 
    def by_finish_date(self, target, finish_date) -> Query(Job):... 
    def by_id(self, target, *ids) -> Query(Job):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Job):... 
    def by_metadata(self, target, *dictionaries) -> Query(Job):... 
    def by_name(self, target, *names) -> Query(Job):... 
    def by_status(self, target, *status) -> Query(Job):... 
    def create(self) -> Job:... 
    def create_batch(self, *attributes) -> Job:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Job:... 
    def get_all(self, projections=None) -> Job:... 
    def get_first(self, projections=None) -> Job:... 
    def get_inputs(self, projections=None) -> Job:... 
    def get_one(self, projections=None) -> Job:... 
    def get_outputs(self, projections=None) -> Job:... 
    def inject(self, filter) -> Query(Job):... 
    def not_by_creation_date(self, target, creation_date) -> Query(Job):... 
    def not_by_data(self, target, *dictionaries) -> Query(Job):... 
    def not_by_finish_date(self, target, finish_date) -> Query(Job):... 
    def not_by_id(self, target, *ids) -> Query(Job):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Job):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Job):... 
    def not_by_name(self, target, *names) -> Query(Job):... 
    def not_by_status(self, target, *status) -> Query(Job):... 


class JobComponent:
    url: object 
    job: Job = Job 
    component_id: str = str() 
    component: Component = Component 
    job_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> JobComponent:... 


class List(Entity):
    category: ListCategory = ListCategory 
    category_id: str = str() 
    user_id: str = str() 
    name: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    project: Project = Project 
    date: str = str() 
    is_open: bool = bool() 
    system_type: str = str() 
    owner: User = User 
    project_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> List:... 
    def by_id(self, target, *ids) -> Query(List):... 
    def by_metadata(self, target, *dictionaries) -> Query(List):... 
    def by_name(self, target, *names) -> Query(List):... 
    def create(self) -> List:... 
    def create_batch(self, *attributes) -> List:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> List:... 
    def get_all(self, projections=None) -> List:... 
    def get_first(self, projections=None) -> List:... 
    def get_inputs(self, projections=None) -> List:... 
    def get_one(self, projections=None) -> List:... 
    def get_outputs(self, projections=None) -> List:... 
    def inject(self, filter) -> Query(List):... 
    def not_by_id(self, target, *ids) -> Query(List):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(List):... 
    def not_by_name(self, target, *names) -> Query(List):... 


class ListCategory(Entity):
    id: str = str() 
    lists: List = List 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListCategory:... 
    def by_id(self, target, *ids) -> Query(ListCategory):... 
    def by_metadata(self, target, *dictionaries) -> Query(ListCategory):... 
    def by_name(self, target, *names) -> Query(ListCategory):... 
    def create(self) -> ListCategory:... 
    def create_batch(self, *attributes) -> ListCategory:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ListCategory:... 
    def get_all(self, projections=None) -> ListCategory:... 
    def get_first(self, projections=None) -> ListCategory:... 
    def get_inputs(self, projections=None) -> ListCategory:... 
    def get_one(self, projections=None) -> ListCategory:... 
    def get_outputs(self, projections=None) -> ListCategory:... 
    def inject(self, filter) -> Query(ListCategory):... 
    def not_by_id(self, target, *ids) -> Query(ListCategory):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ListCategory):... 
    def not_by_name(self, target, *names) -> Query(ListCategory):... 


class ListCustomAttributeLink:
    to_entity_type: str = str() 
    list: List = List 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListCustomAttributeLink:... 


class ListCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    list: List = List 
    configuration_id: str = str() 
    to_id: str = str() 
    from_entity_type: str = str() 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListCustomAttributeLinkFrom:... 


class ListCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListCustomAttributeValue:... 


class ListObject:
    entity_id: str = str() 
    list: List = List 
    id: str = str() 
    list_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListObject:... 


class ListObjectCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ListObjectCustomAttributeValue:... 


class Location(Entity):
    label: str = str() 
    location_components: ComponentLocation = ComponentLocation 
    id: str = str() 
    name: str = str() 
    description: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Location:... 
    def by_id(self, target, *ids) -> Query(Location):... 
    def by_metadata(self, target, *dictionaries) -> Query(Location):... 
    def by_name(self, target, *names) -> Query(Location):... 
    def create(self) -> Location:... 
    def create_batch(self, *attributes) -> Location:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Location:... 
    def get_all(self, projections=None) -> Location:... 
    def get_first(self, projections=None) -> Location:... 
    def get_inputs(self, projections=None) -> Location:... 
    def get_one(self, projections=None) -> Location:... 
    def get_outputs(self, projections=None) -> Location:... 
    def inject(self, filter) -> Query(Location):... 
    def not_by_id(self, target, *ids) -> Query(Location):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Location):... 
    def not_by_name(self, target, *names) -> Query(Location):... 


class Manager:
    user_id: str = str() 
    type_id: str = str() 
    context_id: str = str() 
    user: User = User 
    context: Context = Context 
    type: ManagerType = ManagerType 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Manager:... 


class ManagerType:
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ManagerType:... 


class Membership(Entity):
    user_id: str = str() 
    group_id: str = str() 
    group: Group = Group 
    id: str = str() 
    user: User = User 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Membership:... 
    def by_id(self, target, *ids) -> Query(Membership):... 
    def by_metadata(self, target, *dictionaries) -> Query(Membership):... 
    def create(self) -> Membership:... 
    def create_batch(self, *attributes) -> Membership:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Membership:... 
    def get_all(self, projections=None) -> Membership:... 
    def get_first(self, projections=None) -> Membership:... 
    def get_inputs(self, projections=None) -> Membership:... 
    def get_one(self, projections=None) -> Membership:... 
    def get_outputs(self, projections=None) -> Membership:... 
    def inject(self, filter) -> Query(Membership):... 
    def not_by_id(self, target, *ids) -> Query(Membership):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Membership):... 


class Metadata(Entity):
    parent_id: str = str() 
    parent_type: str = str() 
    key: str = str() 
    value: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Metadata:... 
    def by_id(self, target, *ids) -> Query(Metadata):... 
    def by_metadata(self, target, *dictionaries) -> Query(Metadata):... 
    def create(self) -> Metadata:... 
    def create_batch(self, *attributes) -> Metadata:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Metadata:... 
    def get_all(self, projections=None) -> Metadata:... 
    def get_first(self, projections=None) -> Metadata:... 
    def get_inputs(self, projections=None) -> Metadata:... 
    def get_one(self, projections=None) -> Metadata:... 
    def get_outputs(self, projections=None) -> Metadata:... 
    def inject(self, filter) -> Query(Metadata):... 
    def not_by_id(self, target, *ids) -> Query(Metadata):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Metadata):... 


class Milestone(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Milestone:... 
    def by_assignee(self, target, *assignees) -> Query(Milestone):... 
    def by_id(self, target, *ids) -> Query(Milestone):... 
    def by_incoming_link(self, target, *ids) -> Query(Milestone):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Milestone):... 
    def by_metadata(self, target, *dictionaries) -> Query(Milestone):... 
    def by_name(self, target, *names) -> Query(Milestone):... 
    def by_outgoing_link(self, target, *ids) -> Query(Milestone):... 
    def by_state(self, target, *states) -> Query(Milestone):... 
    def by_status(self, target, *statuses) -> Query(Milestone):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Milestone):... 
    def by_type(self, target, *types) -> Query(Milestone):... 
    def create(self) -> Milestone:... 
    def create_batch(self, *attributes) -> Milestone:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Milestone:... 
    def get_all(self, projections=None) -> Milestone:... 
    def get_first(self, projections=None) -> Milestone:... 
    def get_inputs(self, projections=None) -> Milestone:... 
    def get_one(self, projections=None) -> Milestone:... 
    def get_outputs(self, projections=None) -> Milestone:... 
    def inject(self, filter) -> Query(Milestone):... 
    def link_inputs(self, entity_collection) -> Milestone:... 
    def link_outputs(self, entity_collection) -> Milestone:... 
    def not_by_assignee(self, target, *assignees) -> Query(Milestone):... 
    def not_by_id(self, target, *ids) -> Query(Milestone):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Milestone):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Milestone):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Milestone):... 
    def not_by_name(self, target, *names) -> Query(Milestone):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Milestone):... 
    def not_by_state(self, target, *states) -> Query(Milestone):... 
    def not_by_status(self, target, *statuses) -> Query(Milestone):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Milestone):... 
    def not_by_type(self, target, *types) -> Query(Milestone):... 
    def unlink_inputs(self, entity_collection) -> Milestone:... 
    def unlink_outputs(self, entity_collection) -> Milestone:... 


class Note(Entity):
    in_reply_to_id: str = str() 
    parent_type: str = str() 
    completed_at: str = str() 
    thread_activity: str = str() 
    replies: Note = Note 
    id: str = str() 
    category: NoteCategory = NoteCategory 
    user_id: str = str() 
    author: BaseUser = BaseUser 
    note_components: NoteComponent = NoteComponent 
    content: str = str() 
    parent_id: str = str() 
    project_id: str = str() 
    metadata: typing.List = [Metadata] 
    note_label_links: NoteLabelLink = NoteLabelLink 
    recipients: Recipient = Recipient 
    completed_by_id: str = str() 
    completed_by: User = User 
    date: str = str() 
    in_reply_to: Note = Note 
    project: Project = Project 
    is_todo: bool = bool() 
    category_id: str = str() 
    frame_number: int = int() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Note:... 
    def by_id(self, target, *ids) -> Query(Note):... 
    def by_metadata(self, target, *dictionaries) -> Query(Note):... 
    def by_name(self, target, *names) -> Query(Note):... 
    def create(self) -> Note:... 
    def create_batch(self, *attributes) -> Note:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Note:... 
    def get_all(self, projections=None) -> Note:... 
    def get_first(self, projections=None) -> Note:... 
    def get_inputs(self, projections=None) -> Note:... 
    def get_one(self, projections=None) -> Note:... 
    def get_outputs(self, projections=None) -> Note:... 
    def inject(self, filter) -> Query(Note):... 
    def not_by_id(self, target, *ids) -> Query(Note):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Note):... 
    def not_by_name(self, target, *names) -> Query(Note):... 


class NoteAnnotationComponent:
    component_id: str = str() 
    url: object 
    component: Component = Component 
    note: Note = Note 
    thumbnail_url: object 
    data: object 
    note_id: str = str() 



class NoteCategory(Entity):
    sort: int = int() 
    color: str = str() 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> NoteCategory:... 
    def by_id(self, target, *ids) -> Query(NoteCategory):... 
    def by_metadata(self, target, *dictionaries) -> Query(NoteCategory):... 
    def by_name(self, target, *names) -> Query(NoteCategory):... 
    def create(self) -> NoteCategory:... 
    def create_batch(self, *attributes) -> NoteCategory:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> NoteCategory:... 
    def get_all(self, projections=None) -> NoteCategory:... 
    def get_first(self, projections=None) -> NoteCategory:... 
    def get_inputs(self, projections=None) -> NoteCategory:... 
    def get_one(self, projections=None) -> NoteCategory:... 
    def get_outputs(self, projections=None) -> NoteCategory:... 
    def inject(self, filter) -> Query(NoteCategory):... 
    def not_by_id(self, target, *ids) -> Query(NoteCategory):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(NoteCategory):... 
    def not_by_name(self, target, *names) -> Query(NoteCategory):... 


class NoteComponent(Component):
    component_id: str = str() 
    url: object 
    component: Component = Component 
    note: Note = Note 
    note_id: str = str() 
    thumbnail_url: object 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> NoteComponent:... 
    def by_file_type(self, target, *file_types) -> Query(NoteComponent):... 
    def by_id(self, target, *ids) -> Query(NoteComponent):... 
    def by_location(self, target, *component_locations) -> Query(NoteComponent):... 
    def by_metadata(self, target, *dictionaries) -> Query(NoteComponent):... 
    def by_name(self, target, *names) -> Query(NoteComponent):... 
    def by_resource_identifier(self, target, *resource_identifiers) -> Query(NoteComponent):... 
    def by_size(self, target, minimum=0, maximum=0) -> Query(NoteComponent):... 
    def by_system_type(self, target, *system_types) -> Query(NoteComponent):... 
    def by_version(self, target, *versions) -> Query(NoteComponent):... 
    def create(self) -> NoteComponent:... 
    def create_batch(self, *attributes) -> NoteComponent:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> NoteComponent:... 
    def get_all(self, projections=None) -> NoteComponent:... 
    def get_first(self, projections=None) -> NoteComponent:... 
    def get_inputs(self, projections=None) -> NoteComponent:... 
    def get_one(self, projections=None) -> NoteComponent:... 
    def get_outputs(self, projections=None) -> NoteComponent:... 
    def inject(self, filter) -> Query(NoteComponent):... 
    def not_by_file_type(self, target, *file_types) -> Query(NoteComponent):... 
    def not_by_id(self, target, *ids) -> Query(NoteComponent):... 
    def not_by_location(self, target, *component_locations) -> Query(NoteComponent):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(NoteComponent):... 
    def not_by_name(self, target, *names) -> Query(NoteComponent):... 
    def not_by_resource_identifier(self, target, *resource_identifiers) -> Query(NoteComponent):... 
    def not_by_size(self, target, minimum=0, maximum=0) -> Query(NoteComponent):... 
    def not_by_system_type(self, target, *system_types) -> Query(NoteComponent):... 
    def not_by_version(self, target, *versions) -> Query(NoteComponent):... 


class NoteLabel(Entity):
    sort: int = int() 
    color: str = str() 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> NoteLabel:... 
    def by_id(self, target, *ids) -> Query(NoteLabel):... 
    def by_metadata(self, target, *dictionaries) -> Query(NoteLabel):... 
    def by_name(self, target, *names) -> Query(NoteLabel):... 
    def create(self) -> NoteLabel:... 
    def create_batch(self, *attributes) -> NoteLabel:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> NoteLabel:... 
    def get_all(self, projections=None) -> NoteLabel:... 
    def get_first(self, projections=None) -> NoteLabel:... 
    def get_inputs(self, projections=None) -> NoteLabel:... 
    def get_one(self, projections=None) -> NoteLabel:... 
    def get_outputs(self, projections=None) -> NoteLabel:... 
    def inject(self, filter) -> Query(NoteLabel):... 
    def not_by_id(self, target, *ids) -> Query(NoteLabel):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(NoteLabel):... 
    def not_by_name(self, target, *names) -> Query(NoteLabel):... 


class NoteLabelLink:
    note: Note = Note 
    label_id: str = str() 
    note_id: str = str() 
    label: NoteLabel = NoteLabel 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> NoteLabelLink:... 


class ObjectType(Entity):
    sort: int = int() 
    is_leaf: bool = bool() 
    tasks: Task = Task 
    is_typeable: bool = bool() 
    project_schemas: ProjectSchema = ProjectSchema 
    is_time_reportable: bool = bool() 
    is_schedulable: bool = bool() 
    is_prioritizable: bool = bool() 
    is_statusable: bool = bool() 
    is_taskable: bool = bool() 
    icon: str = str() 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ObjectType:... 
    def by_id(self, target, *ids) -> Query(ObjectType):... 
    def by_metadata(self, target, *dictionaries) -> Query(ObjectType):... 
    def create(self) -> ObjectType:... 
    def create_batch(self, *attributes) -> ObjectType:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ObjectType:... 
    def get_all(self, projections=None) -> ObjectType:... 
    def get_first(self, projections=None) -> ObjectType:... 
    def get_inputs(self, projections=None) -> ObjectType:... 
    def get_one(self, projections=None) -> ObjectType:... 
    def get_outputs(self, projections=None) -> ObjectType:... 
    def inject(self, filter) -> Query(ObjectType):... 
    def not_by_id(self, target, *ids) -> Query(ObjectType):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ObjectType):... 


class Priority:
    sort: int = int() 
    tasks: Task = Task 
    name: str = str() 
    color: str = str() 
    value: float = float() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Priority:... 


class Project(Entity):
    created_at: str = str() 
    managers: Manager = Manager 
    calendar_events: CalendarEvent = CalendarEvent 
    color: str = str() 
    disk_id: str = str() 
    full_name: str = str() 
    disk: Disk = Disk 
    children: Context = Context 
    timelogs: Timelog = Timelog 
    end_date: str = str() 
    parent_id: str = str() 
    created_by: User = User 
    id: str = str() 
    user_security_role_projects: UserSecurityRoleProject = UserSecurityRoleProject 
    start_date: str = str() 
    project_id: str = str() 
    project_schema: ProjectSchema = ProjectSchema 
    metadata: typing.List = [Metadata] 
    status: str = str() 
    scopes: Scope = Scope 
    project_schema_id: str = str() 
    parent: Context = Context 
    descendants: TypedContext = TypedContext 
    thumbnail_id: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    review_sessions: ReviewSession = ReviewSession 
    appointments: Appointment = Appointment 
    link: str = str() 
    review_session_folders: ReviewSessionFolder = ReviewSessionFolder 
    is_private: bool = bool() 
    assets: Asset = Asset 
    is_global: bool = bool() 
    name: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    notes: Note = Note 
    thumbnail: Component = Component 
    assignments: Appointment = Appointment 
    thumbnail_url: object 
    allocations: Appointment = Appointment 
    created_by_id: str = str() 
    _link: str = str() 
    root: str = str() 
    context_type: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Project:... 
    def by_id(self, target, *ids) -> Query(Project):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Project):... 
    def by_metadata(self, target, *dictionaries) -> Query(Project):... 
    def by_name(self, target, *names) -> Query(Project):... 
    def by_status(self, target, status) -> Query(Project):... 
    def create(self, name, project_schema) -> Project:... 
    def create_batch(self, *attributes) -> Project:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Project:... 
    def get_all(self, projections=None) -> Project:... 
    def get_first(self, projections=None) -> Project:... 
    def get_inputs(self, projections=None) -> Project:... 
    def get_one(self, projections=None) -> Project:... 
    def get_outputs(self, projections=None) -> Project:... 
    def inject(self, filter) -> Query(Project):... 
    def not_by_id(self, target, *ids) -> Query(Project):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Project):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Project):... 
    def not_by_name(self, target, *names) -> Query(Project):... 
    def not_by_status(self, target, status) -> Query(Project):... 


class ProjectSchema(Entity):
    _task_workflow: WorkflowSchema = WorkflowSchema 
    asset_version_workflow_schema_id: str = str() 
    _schemas: Schema = Schema 
    task_workflow_schema_id: str = str() 
    _overrides: ProjectSchemaOverride = ProjectSchemaOverride 
    _task_type_schema: TaskTypeSchema = TaskTypeSchema 
    task_workflow_schema: WorkflowSchema = WorkflowSchema 
    object_types: ObjectType = ObjectType 
    _version_workflow: WorkflowSchema = WorkflowSchema 
    asset_version_workflow_schema: WorkflowSchema = WorkflowSchema 
    id: str = str() 
    task_workflow_schema_overrides: ProjectSchemaOverride = ProjectSchemaOverride 
    task_type_schema_id: str = str() 
    task_type_schema: TaskTypeSchema = TaskTypeSchema 
    task_templates: TaskTemplate = TaskTemplate 
    object_type_schemas: Schema = Schema 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ProjectSchema:... 
    def by_id(self, target, *ids) -> Query(ProjectSchema):... 
    def by_metadata(self, target, *dictionaries) -> Query(ProjectSchema):... 
    def create(self) -> ProjectSchema:... 
    def create_batch(self, *attributes) -> ProjectSchema:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ProjectSchema:... 
    def get_all(self, projections=None) -> ProjectSchema:... 
    def get_first(self, projections=None) -> ProjectSchema:... 
    def get_inputs(self, projections=None) -> ProjectSchema:... 
    def get_one(self, projections=None) -> ProjectSchema:... 
    def get_outputs(self, projections=None) -> ProjectSchema:... 
    def inject(self, filter) -> Query(ProjectSchema):... 
    def not_by_id(self, target, *ids) -> Query(ProjectSchema):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ProjectSchema):... 


class ProjectSchemaObjectType:
    object_type: ObjectType = ObjectType 
    project_schema_id: str = str() 
    project_schema: ProjectSchema = ProjectSchema 
    object_type_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ProjectSchemaObjectType:... 


class ProjectSchemaOverride:
    project_schema_id: str = str() 
    workflow_schema_id: str = str() 
    workflow_schema: WorkflowSchema = WorkflowSchema 
    id: str = str() 
    type_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ProjectSchemaOverride:... 


class Recipient(Entity):
    note_id: str = str() 
    resource_id: str = str() 
    text_mentioned: str = str() 
    note: Note = Note 
    user: User = User 
    recipient: Resource = Resource 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Recipient:... 
    def by_id(self, target, *ids) -> Query(Recipient):... 
    def by_metadata(self, target, *dictionaries) -> Query(Recipient):... 
    def create(self) -> Recipient:... 
    def create_batch(self, *attributes) -> Recipient:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Recipient:... 
    def get_all(self, projections=None) -> Recipient:... 
    def get_first(self, projections=None) -> Recipient:... 
    def get_inputs(self, projections=None) -> Recipient:... 
    def get_one(self, projections=None) -> Recipient:... 
    def get_outputs(self, projections=None) -> Recipient:... 
    def inject(self, filter) -> Query(Recipient):... 
    def not_by_id(self, target, *ids) -> Query(Recipient):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Recipient):... 


class Resource(Entity):
    assignments: Appointment = Appointment 
    dashboard_resources: DashboardResource = DashboardResource 
    appointments: Appointment = Appointment 
    allocations: Appointment = Appointment 
    id: str = str() 
    resource_type: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Resource:... 
    def by_id(self, target, *ids) -> Query(Resource):... 
    def by_metadata(self, target, *dictionaries) -> Query(Resource):... 
    def create(self) -> Resource:... 
    def create_batch(self, *attributes) -> Resource:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Resource:... 
    def get_all(self, projections=None) -> Resource:... 
    def get_first(self, projections=None) -> Resource:... 
    def get_inputs(self, projections=None) -> Resource:... 
    def get_one(self, projections=None) -> Resource:... 
    def get_outputs(self, projections=None) -> Resource:... 
    def inject(self, filter) -> Query(Resource):... 
    def not_by_id(self, target, *ids) -> Query(Resource):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Resource):... 


class ReviewSession(Entity):
    passphrase_enabled: bool = bool() 
    is_open: bool = bool() 
    review_session_folder: ReviewSessionFolder = ReviewSessionFolder 
    passphrase: str = str() 
    id: str = str() 
    shareable_url_enabled: bool = bool() 
    review_session_invitees: ReviewSessionInvitee = ReviewSessionInvitee 
    created_by: User = User 
    availability: str = str() 
    project_id: str = str() 
    start_date: str = str() 
    description: str = str() 
    end_date: str = str() 
    thumbnail_id: str = str() 
    review_session_folder_id: str = str() 
    name: str = str() 
    review_session_objects: ReviewSessionObject = ReviewSessionObject 
    settings: EntitySetting = EntitySetting 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    thumbnail_url: object 
    is_moderated: bool = bool() 
    created_by_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ReviewSession:... 
    def by_id(self, target, *ids) -> Query(ReviewSession):... 
    def by_metadata(self, target, *dictionaries) -> Query(ReviewSession):... 
    def by_name(self, target, *names) -> Query(ReviewSession):... 
    def create(self, name, project_schema) -> ReviewSession:... 
    def create_batch(self, *attributes) -> ReviewSession:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ReviewSession:... 
    def get_all(self, projections=None) -> ReviewSession:... 
    def get_first(self, projections=None) -> ReviewSession:... 
    def get_inputs(self, projections=None) -> ReviewSession:... 
    def get_one(self, projections=None) -> ReviewSession:... 
    def get_outputs(self, projections=None) -> ReviewSession:... 
    def inject(self, filter) -> Query(ReviewSession):... 
    def not_by_id(self, target, *ids) -> Query(ReviewSession):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ReviewSession):... 
    def not_by_name(self, target, *names) -> Query(ReviewSession):... 


class ReviewSessionFolder:
    project: Project = Project 
    id: str = str() 
    project_id: str = str() 
    name: str = str() 
    review_sessions: ReviewSession = ReviewSession 



class ReviewSessionInvitee(Entity):
    created_from_shared_url: bool = bool() 
    resource: Resource = Resource 
    name: str = str() 
    resource_id: str = str() 
    created_at: str = str() 
    created_by: User = User 
    id: str = str() 
    review_session_id: str = str() 
    last_sent_at: str = str() 
    created_by_id: str = str() 
    email: str = str() 
    statuses: ReviewSessionObjectStatus = ReviewSessionObjectStatus 
    review_session: ReviewSession = ReviewSession 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ReviewSessionInvitee:... 
    def by_id(self, target, *ids) -> Query(ReviewSessionInvitee):... 
    def by_metadata(self, target, *dictionaries) -> Query(ReviewSessionInvitee):... 
    def create(self) -> ReviewSessionInvitee:... 
    def create_batch(self, *attributes) -> ReviewSessionInvitee:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ReviewSessionInvitee:... 
    def get_all(self, projections=None) -> ReviewSessionInvitee:... 
    def get_first(self, projections=None) -> ReviewSessionInvitee:... 
    def get_inputs(self, projections=None) -> ReviewSessionInvitee:... 
    def get_one(self, projections=None) -> ReviewSessionInvitee:... 
    def get_outputs(self, projections=None) -> ReviewSessionInvitee:... 
    def inject(self, filter) -> Query(ReviewSessionInvitee):... 
    def not_by_id(self, target, *ids) -> Query(ReviewSessionInvitee):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ReviewSessionInvitee):... 


class ReviewSessionObject(Entity):
    name: str = str() 
    created_at: str = str() 
    description: str = str() 
    version_id: str = str() 
    id: str = str() 
    review_session_id: str = str() 
    version: str = str() 
    notes: Note = Note 
    asset_version: AssetVersion = AssetVersion 
    sort_order: float = float() 
    annotations: ReviewSessionObjectAnnotation = ReviewSessionObjectAnnotation 
    statuses: ReviewSessionObjectStatus = ReviewSessionObjectStatus 
    review_session: ReviewSession = ReviewSession 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ReviewSessionObject:... 
    def by_id(self, target, *ids) -> Query(ReviewSessionObject):... 
    def by_metadata(self, target, *dictionaries) -> Query(ReviewSessionObject):... 
    def create(self) -> ReviewSessionObject:... 
    def create_batch(self, *attributes) -> ReviewSessionObject:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ReviewSessionObject:... 
    def get_all(self, projections=None) -> ReviewSessionObject:... 
    def get_first(self, projections=None) -> ReviewSessionObject:... 
    def get_inputs(self, projections=None) -> ReviewSessionObject:... 
    def get_one(self, projections=None) -> ReviewSessionObject:... 
    def get_outputs(self, projections=None) -> ReviewSessionObject:... 
    def inject(self, filter) -> Query(ReviewSessionObject):... 
    def not_by_id(self, target, *ids) -> Query(ReviewSessionObject):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ReviewSessionObject):... 


class ReviewSessionObjectAnnotation:
    created_at: str = str() 
    review_session_object_id: str = str() 
    updated_at: str = str() 
    id: str = str() 
    review_session_object: ReviewSessionObject = ReviewSessionObject 
    data: str = str() 
    frame_number: int = int() 



class ReviewSessionObjectAnnotationComponent:
    component_id: str = str() 
    url: object 
    review_session_object_id: str = str() 
    component: Component = Component 
    thumbnail_url: object 
    review_session_object: ReviewSessionObject = ReviewSessionObject 
    frame_number: str = str() 



class ReviewSessionObjectStatus(Entity):
    status: str = str() 
    review_session_object_id: str = str() 
    resource: Resource = Resource 
    resource_id: str = str() 
    created_at: str = str() 
    invitee: ReviewSessionInvitee = ReviewSessionInvitee 
    review_session_object: ReviewSessionObject = ReviewSessionObject 
    review_session_invitee_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> ReviewSessionObjectStatus:... 
    def by_id(self, target, *ids) -> Query(ReviewSessionObjectStatus):... 
    def by_metadata(self, target, *dictionaries) -> Query(ReviewSessionObjectStatus):... 
    def create(self) -> ReviewSessionObjectStatus:... 
    def create_batch(self, *attributes) -> ReviewSessionObjectStatus:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> ReviewSessionObjectStatus:... 
    def get_all(self, projections=None) -> ReviewSessionObjectStatus:... 
    def get_first(self, projections=None) -> ReviewSessionObjectStatus:... 
    def get_inputs(self, projections=None) -> ReviewSessionObjectStatus:... 
    def get_one(self, projections=None) -> ReviewSessionObjectStatus:... 
    def get_outputs(self, projections=None) -> ReviewSessionObjectStatus:... 
    def inject(self, filter) -> Query(ReviewSessionObjectStatus):... 
    def not_by_id(self, target, *ids) -> Query(ReviewSessionObjectStatus):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(ReviewSessionObjectStatus):... 


class Scene(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Scene:... 
    def by_assignee(self, target, *assignees) -> Query(Scene):... 
    def by_id(self, target, *ids) -> Query(Scene):... 
    def by_incoming_link(self, target, *ids) -> Query(Scene):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Scene):... 
    def by_metadata(self, target, *dictionaries) -> Query(Scene):... 
    def by_name(self, target, *names) -> Query(Scene):... 
    def by_outgoing_link(self, target, *ids) -> Query(Scene):... 
    def by_state(self, target, *states) -> Query(Scene):... 
    def by_status(self, target, *statuses) -> Query(Scene):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Scene):... 
    def by_type(self, target, *types) -> Query(Scene):... 
    def create(self) -> Scene:... 
    def create_batch(self, *attributes) -> Scene:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Scene:... 
    def get_all(self, projections=None) -> Scene:... 
    def get_first(self, projections=None) -> Scene:... 
    def get_inputs(self, projections=None) -> Scene:... 
    def get_one(self, projections=None) -> Scene:... 
    def get_outputs(self, projections=None) -> Scene:... 
    def inject(self, filter) -> Query(Scene):... 
    def link_inputs(self, entity_collection) -> Scene:... 
    def link_outputs(self, entity_collection) -> Scene:... 
    def not_by_assignee(self, target, *assignees) -> Query(Scene):... 
    def not_by_id(self, target, *ids) -> Query(Scene):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Scene):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Scene):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Scene):... 
    def not_by_name(self, target, *names) -> Query(Scene):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Scene):... 
    def not_by_state(self, target, *states) -> Query(Scene):... 
    def not_by_status(self, target, *statuses) -> Query(Scene):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Scene):... 
    def not_by_type(self, target, *types) -> Query(Scene):... 
    def unlink_inputs(self, entity_collection) -> Scene:... 
    def unlink_outputs(self, entity_collection) -> Scene:... 


class Schema:
    project_schema_id: str = str() 
    type_id: str = str() 
    statuses: SchemaStatus = SchemaStatus 
    object_type_id: str = str() 
    id: str = str() 
    types: SchemaType = SchemaType 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Schema:... 


class SchemaStatus:
    sort: int = int() 
    schema_id: str = str() 
    task_status: Status = Status 
    status_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> SchemaStatus:... 


class SchemaType:
    sort: int = int() 
    schema_id: str = str() 
    task_type: Type = Type 
    type_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> SchemaType:... 


class Scope:
    name: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Scope:... 


class SecurityRole(Entity):
    user_security_roles: UserSecurityRole = UserSecurityRole 
    type: str = str() 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> SecurityRole:... 
    def by_id(self, target, *ids) -> Query(SecurityRole):... 
    def by_metadata(self, target, *dictionaries) -> Query(SecurityRole):... 
    def create(self) -> SecurityRole:... 
    def create_batch(self, *attributes) -> SecurityRole:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> SecurityRole:... 
    def get_all(self, projections=None) -> SecurityRole:... 
    def get_first(self, projections=None) -> SecurityRole:... 
    def get_inputs(self, projections=None) -> SecurityRole:... 
    def get_one(self, projections=None) -> SecurityRole:... 
    def get_outputs(self, projections=None) -> SecurityRole:... 
    def inject(self, filter) -> Query(SecurityRole):... 
    def not_by_id(self, target, *ids) -> Query(SecurityRole):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(SecurityRole):... 


class Sequence(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Sequence:... 
    def by_assignee(self, target, *assignees) -> Query(Sequence):... 
    def by_id(self, target, *ids) -> Query(Sequence):... 
    def by_incoming_link(self, target, *ids) -> Query(Sequence):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Sequence):... 
    def by_metadata(self, target, *dictionaries) -> Query(Sequence):... 
    def by_name(self, target, *names) -> Query(Sequence):... 
    def by_outgoing_link(self, target, *ids) -> Query(Sequence):... 
    def by_state(self, target, *states) -> Query(Sequence):... 
    def by_status(self, target, *statuses) -> Query(Sequence):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Sequence):... 
    def by_type(self, target, *types) -> Query(Sequence):... 
    def create(self, name) -> Sequence:... 
    def create_batch(self, *attributes) -> Sequence:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Sequence:... 
    def get_all(self, projections=None) -> Sequence:... 
    def get_first(self, projections=None) -> Sequence:... 
    def get_inputs(self, projections=None) -> Sequence:... 
    def get_one(self, projections=None) -> Sequence:... 
    def get_outputs(self, projections=None) -> Sequence:... 
    def inject(self, filter) -> Query(Sequence):... 
    def link_inputs(self, entity_collection) -> Sequence:... 
    def link_outputs(self, entity_collection) -> Sequence:... 
    def not_by_assignee(self, target, *assignees) -> Query(Sequence):... 
    def not_by_id(self, target, *ids) -> Query(Sequence):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Sequence):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Sequence):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Sequence):... 
    def not_by_name(self, target, *names) -> Query(Sequence):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Sequence):... 
    def not_by_state(self, target, *states) -> Query(Sequence):... 
    def not_by_status(self, target, *statuses) -> Query(Sequence):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Sequence):... 
    def not_by_type(self, target, *types) -> Query(Sequence):... 
    def unlink_inputs(self, entity_collection) -> Sequence:... 
    def unlink_outputs(self, entity_collection) -> Sequence:... 


class SequenceComponent:
    container: ContainerComponent = ContainerComponent 
    name: str = str() 
    component_locations: ComponentLocation = ComponentLocation 
    file_type: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    container_id: str = str() 
    version_id: str = str() 
    padding: int = int() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    version: AssetVersion = AssetVersion 
    system_type: str = str() 
    members: Component = Component 
    size: int = int() 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> SequenceComponent:... 


class Setting:
    group: str = str() 
    name: str = str() 
    value: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Setting:... 


class SettingComponent:
    component_id: str = str() 
    group: str = str() 
    name: str = str() 
    url: object 
    component: Component = Component 
    setting: Setting = Setting 
    thumbnail_url: object 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> SettingComponent:... 


class Shot(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Shot:... 
    def by_assignee(self, target, *assignees) -> Query(Shot):... 
    def by_id(self, target, *ids) -> Query(Shot):... 
    def by_incoming_link(self, target, *ids) -> Query(Shot):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Shot):... 
    def by_metadata(self, target, *dictionaries) -> Query(Shot):... 
    def by_name(self, target, *names) -> Query(Shot):... 
    def by_outgoing_link(self, target, *ids) -> Query(Shot):... 
    def by_state(self, target, *states) -> Query(Shot):... 
    def by_status(self, target, *statuses) -> Query(Shot):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Shot):... 
    def by_type(self, target, *types) -> Query(Shot):... 
    def create(self, name) -> Shot:... 
    def create_batch(self, *attributes) -> Shot:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Shot:... 
    def get_all(self, projections=None) -> Shot:... 
    def get_first(self, projections=None) -> Shot:... 
    def get_inputs(self, projections=None) -> Shot:... 
    def get_one(self, projections=None) -> Shot:... 
    def get_outputs(self, projections=None) -> Shot:... 
    def inject(self, filter) -> Query(Shot):... 
    def link_inputs(self, entity_collection) -> Shot:... 
    def link_outputs(self, entity_collection) -> Shot:... 
    def not_by_assignee(self, target, *assignees) -> Query(Shot):... 
    def not_by_id(self, target, *ids) -> Query(Shot):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Shot):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Shot):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Shot):... 
    def not_by_name(self, target, *names) -> Query(Shot):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Shot):... 
    def not_by_state(self, target, *states) -> Query(Shot):... 
    def not_by_status(self, target, *statuses) -> Query(Shot):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Shot):... 
    def not_by_type(self, target, *types) -> Query(Shot):... 
    def unlink_inputs(self, entity_collection) -> Shot:... 
    def unlink_outputs(self, entity_collection) -> Shot:... 


class SplitTaskPart:
    task: Task = Task 
    end_date: str = str() 
    task_id: str = str() 
    label: str = str() 
    id: str = str() 
    start_date: str = str() 



class State(Entity):
    short: str = str() 
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> State:... 
    def by_id(self, target, *ids) -> Query(State):... 
    def by_metadata(self, target, *dictionaries) -> Query(State):... 
    def create(self) -> State:... 
    def create_batch(self, *attributes) -> State:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> State:... 
    def get_all(self, projections=None) -> State:... 
    def get_first(self, projections=None) -> State:... 
    def get_inputs(self, projections=None) -> State:... 
    def get_one(self, projections=None) -> State:... 
    def get_outputs(self, projections=None) -> State:... 
    def inject(self, filter) -> Query(State):... 
    def not_by_id(self, target, *ids) -> Query(State):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(State):... 


class Status(Entity):
    sort: int = int() 
    tasks: Task = Task 
    name: str = str() 
    color: str = str() 
    is_active: bool = bool() 
    state: State = State 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Status:... 
    def by_id(self, target, *ids) -> Query(Status):... 
    def by_metadata(self, target, *dictionaries) -> Query(Status):... 
    def by_name(self, target, *names) -> Query(Status):... 
    def create(self) -> Status:... 
    def create_batch(self, *attributes) -> Status:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Status:... 
    def get_all(self, projections=None) -> Status:... 
    def get_first(self, projections=None) -> Status:... 
    def get_inputs(self, projections=None) -> Status:... 
    def get_one(self, projections=None) -> Status:... 
    def get_outputs(self, projections=None) -> Status:... 
    def inject(self, filter) -> Query(Status):... 
    def not_by_id(self, target, *ids) -> Query(Status):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Status):... 
    def not_by_name(self, target, *names) -> Query(Status):... 


class StatusChange:
    status: Status = Status 
    user_id: str = str() 
    status_id: str = str() 
    parent_type: str = str() 
    parent_id: str = str() 
    user: User = User 
    from_status: Status = Status 
    date: str = str() 
    from_status_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> StatusChange:... 


class StatusRule:
    status: Status = Status 
    status_rule_group_id: str = str() 
    id: str = str() 
    status_rule_group: StatusRuleGroup = StatusRuleGroup 
    status_id: str = str() 



class StatusRuleGroup:
    status: Status = Status 
    status_rules: StatusRule = StatusRule 
    entity_type: str = str() 
    status_id: str = str() 
    role_id: str = str() 
    schema_id: str = str() 
    role: SecurityRole = SecurityRole 
    id: str = str() 
    schema: ProjectSchema = ProjectSchema 



class Task(TypedContext):
    status: Status = Status 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    _link: str = str() 
    incoming_links: TypedContextLink = TypedContextLink 
    id: str = str() 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    parent: Context = Context 
    assignments: Appointment = Appointment 
    descendants: TypedContext = TypedContext 
    created_by: User = User 
    children: Context = Context 
    priority: Priority = Priority 
    parent_id: str = str() 
    start_date: str = str() 
    project_id: str = str() 
    type: Type = Type 
    thumbnail: Component = Component 
    metadata: typing.List = [Metadata] 
    sort: float = float() 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    end_date: str = str() 
    status_id: str = str() 
    thumbnail_id: str = str() 
    bid: float = float() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    name: str = str() 
    assets: Asset = Asset 
    context_type: str = str() 
    created_at: str = str() 
    thumbnail_source_id: str = str() 
    project: Project = Project 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Task:... 
    def by_assignee(self, target, *assignees) -> Query(Task):... 
    def by_id(self, target, *ids) -> Query(Task):... 
    def by_incoming_link(self, target, *ids) -> Query(Task):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Task):... 
    def by_metadata(self, target, *dictionaries) -> Query(Task):... 
    def by_name(self, target, *names) -> Query(Task):... 
    def by_outgoing_link(self, target, *ids) -> Query(Task):... 
    def by_state(self, target, *states) -> Query(Task):... 
    def by_status(self, target, *statuses) -> Query(Task):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(Task):... 
    def by_type(self, target, *types) -> Query(Task):... 
    def create(self, name, task_type) -> Task:... 
    def create_batch(self, *attributes) -> Task:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Task:... 
    def get_all(self, projections=None) -> Task:... 
    def get_first(self, projections=None) -> Task:... 
    def get_inputs(self, projections=None) -> Task:... 
    def get_one(self, projections=None) -> Task:... 
    def get_outputs(self, projections=None) -> Task:... 
    def inject(self, filter) -> Query(Task):... 
    def link_inputs(self, entity_collection) -> Task:... 
    def link_outputs(self, entity_collection) -> Task:... 
    def not_by_assignee(self, target, *assignees) -> Query(Task):... 
    def not_by_id(self, target, *ids) -> Query(Task):... 
    def not_by_incoming_link(self, target, *ids) -> Query(Task):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Task):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Task):... 
    def not_by_name(self, target, *names) -> Query(Task):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(Task):... 
    def not_by_state(self, target, *states) -> Query(Task):... 
    def not_by_status(self, target, *statuses) -> Query(Task):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(Task):... 
    def not_by_type(self, target, *types) -> Query(Task):... 
    def unlink_inputs(self, entity_collection) -> Task:... 
    def unlink_outputs(self, entity_collection) -> Task:... 


class TaskTemplate:
    items: TaskTemplateItem = TaskTemplateItem 
    project_schema_id: str = str() 
    project_schema: ProjectSchema = ProjectSchema 
    name: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TaskTemplate:... 


class TaskTemplateItem:
    task_type: Type = Type 
    template_id: str = str() 
    id: str = str() 
    task_type_id: str = str() 
    template: TaskTemplate = TaskTemplate 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TaskTemplateItem:... 


class TaskTypeSchema(Entity):
    id: str = str() 
    types: Type = Type 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TaskTypeSchema:... 
    def by_id(self, target, *ids) -> Query(TaskTypeSchema):... 
    def by_metadata(self, target, *dictionaries) -> Query(TaskTypeSchema):... 
    def create(self) -> TaskTypeSchema:... 
    def create_batch(self, *attributes) -> TaskTypeSchema:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> TaskTypeSchema:... 
    def get_all(self, projections=None) -> TaskTypeSchema:... 
    def get_first(self, projections=None) -> TaskTypeSchema:... 
    def get_inputs(self, projections=None) -> TaskTypeSchema:... 
    def get_one(self, projections=None) -> TaskTypeSchema:... 
    def get_outputs(self, projections=None) -> TaskTypeSchema:... 
    def inject(self, filter) -> Query(TaskTypeSchema):... 
    def not_by_id(self, target, *ids) -> Query(TaskTypeSchema):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(TaskTypeSchema):... 


class TaskTypeSchemaType:
    task_type_schema_id: str = str() 
    type_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TaskTypeSchemaType:... 


class Timelog(Entity):
    comment: str = str() 
    time_zone_offset: float = float() 
    user_id: str = str() 
    name: str = str() 
    context_id: str = str() 
    start: str = str() 
    user: User = User 
    context: Context = Context 
    duration: float = float() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Timelog:... 
    def by_id(self, target, *ids) -> Query(Timelog):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(Timelog):... 
    def by_metadata(self, target, *dictionaries) -> Query(Timelog):... 
    def by_name(self, target, *names) -> Query(Timelog):... 
    def create(self) -> Timelog:... 
    def create_batch(self, *attributes) -> Timelog:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Timelog:... 
    def get_all(self, projections=None) -> Timelog:... 
    def get_first(self, projections=None) -> Timelog:... 
    def get_inputs(self, projections=None) -> Timelog:... 
    def get_one(self, projections=None) -> Timelog:... 
    def get_outputs(self, projections=None) -> Timelog:... 
    def inject(self, filter) -> Query(Timelog):... 
    def not_by_id(self, target, *ids) -> Query(Timelog):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(Timelog):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Timelog):... 
    def not_by_name(self, target, *names) -> Query(Timelog):... 


class Timer:
    comment: str = str() 
    user_id: str = str() 
    name: str = str() 
    context_id: str = str() 
    start: str = str() 
    user: User = User 
    context: Context = Context 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Timer:... 


class Type(Entity):
    sort: int = int() 
    tasks: Task = Task 
    name: str = str() 
    task_type_schemas: TaskTypeSchema = TaskTypeSchema 
    color: str = str() 
    is_billable: bool = bool() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> Type:... 
    def by_id(self, target, *ids) -> Query(Type):... 
    def by_metadata(self, target, *dictionaries) -> Query(Type):... 
    def create(self) -> Type:... 
    def create_batch(self, *attributes) -> Type:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> Type:... 
    def get_all(self, projections=None) -> Type:... 
    def get_first(self, projections=None) -> Type:... 
    def get_inputs(self, projections=None) -> Type:... 
    def get_one(self, projections=None) -> Type:... 
    def get_outputs(self, projections=None) -> Type:... 
    def inject(self, filter) -> Query(Type):... 
    def not_by_id(self, target, *ids) -> Query(Type):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(Type):... 


class TypedContext(Entity):
    sort: float = float() 
    managers: Manager = Manager 
    type_id: str = str() 
    priority_id: str = str() 
    status_changes: StatusChange = StatusChange 
    created_by: User = User 
    incoming_links: TypedContextLink = TypedContextLink 
    thumbnail_source_id: str = str() 
    children: Context = Context 
    timelogs: Timelog = Timelog 
    ancestors: TypedContext = TypedContext 
    end_date: str = str() 
    status_id: str = str() 
    _link: str = str() 
    id: str = str() 
    priority: Priority = Priority 
    parent_id: str = str() 
    project_id: str = str() 
    type: Type = Type 
    start_date: str = str() 
    metadata: typing.List = [Metadata] 
    status: Status = Status 
    scopes: Scope = Scope 
    object_type: ObjectType = ObjectType 
    description: str = str() 
    parent: Context = Context 
    descendants: TypedContext = TypedContext 
    thumbnail_id: str = str() 
    bid: float = float() 
    context_type: str = str() 
    lists: TypedContextList = TypedContextList 
    appointments: Appointment = Appointment 
    link: str = str() 
    time_logged: float = float() 
    bid_time_logged_difference: float = float() 
    assets: Asset = Asset 
    name: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    created_at: str = str() 
    thumbnail: Component = Component 
    project: Project = Project 
    assignments: Appointment = Appointment 
    thumbnail_url: object 
    split_parts: SplitTaskPart = SplitTaskPart 
    object_type_id: str = str() 
    created_by_id: str = str() 
    outgoing_links: TypedContextLink = TypedContextLink 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    notes: Note = Note 
    allocations: Appointment = Appointment 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TypedContext:... 
    def by_assignee(self, target, *assignees) -> Query(TypedContext):... 
    def by_id(self, target, *ids) -> Query(TypedContext):... 
    def by_incoming_link(self, target, *ids) -> Query(TypedContext):... 
    def by_lifespan(self, target, start=None, end=None) -> Query(TypedContext):... 
    def by_metadata(self, target, *dictionaries) -> Query(TypedContext):... 
    def by_name(self, target, *names) -> Query(TypedContext):... 
    def by_outgoing_link(self, target, *ids) -> Query(TypedContext):... 
    def by_state(self, target, *states) -> Query(TypedContext):... 
    def by_status(self, target, *statuses) -> Query(TypedContext):... 
    def by_status_change_time(self, target, start=None, end=None) -> Query(TypedContext):... 
    def by_type(self, target, *types) -> Query(TypedContext):... 
    def create(self) -> TypedContext:... 
    def create_batch(self, *attributes) -> TypedContext:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> TypedContext:... 
    def get_all(self, projections=None) -> TypedContext:... 
    def get_first(self, projections=None) -> TypedContext:... 
    def get_inputs(self, projections=None) -> TypedContext:... 
    def get_one(self, projections=None) -> TypedContext:... 
    def get_outputs(self, projections=None) -> TypedContext:... 
    def inject(self, filter) -> Query(TypedContext):... 
    def link_inputs(self, entity_collection) -> TypedContext:... 
    def link_outputs(self, entity_collection) -> TypedContext:... 
    def not_by_assignee(self, target, *assignees) -> Query(TypedContext):... 
    def not_by_id(self, target, *ids) -> Query(TypedContext):... 
    def not_by_incoming_link(self, target, *ids) -> Query(TypedContext):... 
    def not_by_lifespan(self, target, start=None, end=None) -> Query(TypedContext):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(TypedContext):... 
    def not_by_name(self, target, *names) -> Query(TypedContext):... 
    def not_by_outgoing_link(self, target, *ids) -> Query(TypedContext):... 
    def not_by_state(self, target, *states) -> Query(TypedContext):... 
    def not_by_status(self, target, *statuses) -> Query(TypedContext):... 
    def not_by_status_change_time(self, target, start=None, end=None) -> Query(TypedContext):... 
    def not_by_type(self, target, *types) -> Query(TypedContext):... 
    def unlink_inputs(self, entity_collection) -> TypedContext:... 
    def unlink_outputs(self, entity_collection) -> TypedContext:... 


class TypedContextLink(Entity):
    from: TypedContext = TypedContext 
    lag: float = float() 
    to_id: str = str() 
    to: TypedContext = TypedContext 
    from_id: str = str() 
    type: str = str() 
    id: str = str() 
    metadata: typing.List = [Metadata] 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TypedContextLink:... 
    def by_id(self, target, *ids) -> Query(TypedContextLink):... 
    def by_metadata(self, target, *dictionaries) -> Query(TypedContextLink):... 
    def create(self) -> TypedContextLink:... 
    def create_batch(self, *attributes) -> TypedContextLink:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> TypedContextLink:... 
    def get_all(self, projections=None) -> TypedContextLink:... 
    def get_first(self, projections=None) -> TypedContextLink:... 
    def get_inputs(self, projections=None) -> TypedContextLink:... 
    def get_one(self, projections=None) -> TypedContextLink:... 
    def get_outputs(self, projections=None) -> TypedContextLink:... 
    def inject(self, filter) -> Query(TypedContextLink):... 
    def not_by_id(self, target, *ids) -> Query(TypedContextLink):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(TypedContextLink):... 


class TypedContextList(List):
    category: ListCategory = ListCategory 
    project_id: str = str() 
    user_id: str = str() 
    name: str = str() 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    items: Task = Task 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    project: Project = Project 
    owner: User = User 
    is_open: bool = bool() 
    system_type: str = str() 
    date: str = str() 
    category_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TypedContextList:... 
    def by_id(self, target, *ids) -> Query(TypedContextList):... 
    def by_metadata(self, target, *dictionaries) -> Query(TypedContextList):... 
    def by_name(self, target, *names) -> Query(TypedContextList):... 
    def create(self) -> TypedContextList:... 
    def create_batch(self, *attributes) -> TypedContextList:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> TypedContextList:... 
    def get_all(self, projections=None) -> TypedContextList:... 
    def get_first(self, projections=None) -> TypedContextList:... 
    def get_inputs(self, projections=None) -> TypedContextList:... 
    def get_one(self, projections=None) -> TypedContextList:... 
    def get_outputs(self, projections=None) -> TypedContextList:... 
    def inject(self, filter) -> Query(TypedContextList):... 
    def not_by_id(self, target, *ids) -> Query(TypedContextList):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(TypedContextList):... 
    def not_by_name(self, target, *names) -> Query(TypedContextList):... 


class TypedContextStatusChange:
    status: Status = Status 
    user_id: str = str() 
    parent: TypedContext = TypedContext 
    status_id: str = str() 
    parent_type: str = str() 
    parent_id: str = str() 
    user: User = User 
    from_status: Status = Status 
    date: str = str() 
    from_status_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> TypedContextStatusChange:... 


class TypedContextStatusRuleGroup:
    status: Status = Status 
    status_id: str = str() 
    status_rules: StatusRule = StatusRule 
    entity_type: str = str() 
    object_type: ObjectType = ObjectType 
    role_id: str = str() 
    schema_id: str = str() 
    role: SecurityRole = SecurityRole 
    object_type_id: str = str() 
    id: str = str() 
    schema: ProjectSchema = ProjectSchema 



class User(Entity):
    last_name: str = str() 
    user_type: UserType = UserType 
    user_type_id: str = str() 
    id: str = str() 
    timelogs: Timelog = Timelog 
    is_otp_enabled: bool = bool() 
    assignments: Appointment = Appointment 
    require_details_update: bool = bool() 
    email: str = str() 
    metadata: typing.List = [Metadata] 
    username: str = str() 
    user_security_roles: UserSecurityRole = UserSecurityRole 
    thumbnail_id: str = str() 
    custom_attribute_links_from: typing.List = [CustomAttributeLinkFrom] 
    is_active: bool = bool() 
    first_name: str = str() 
    dashboard_resources: DashboardResource = DashboardResource 
    appointments: Appointment = Appointment 
    custom_attribute_links: typing.List = [CustomAttributeLink] 
    thumbnail: Component = Component 
    memberships: Membership = Membership 
    is_totp_enabled: bool = bool() 
    thumbnail_url: object 
    allocations: Appointment = Appointment 
    resource_type: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> User:... 
    def by_active_state(self, target, *states) -> Query(User):... 
    def by_id(self, target, *ids) -> Query(User):... 
    def by_metadata(self, target, *dictionaries) -> Query(User):... 
    def by_name(self, target, *names) -> Query(User):... 
    def create(self) -> User:... 
    def create_batch(self, *attributes) -> User:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> User:... 
    def get_all(self, projections=None) -> User:... 
    def get_first(self, projections=None) -> User:... 
    def get_inputs(self, projections=None) -> User:... 
    def get_one(self, projections=None) -> User:... 
    def get_outputs(self, projections=None) -> User:... 
    def inject(self, filter) -> Query(User):... 
    def not_by_active_state(self, target, *states) -> Query(User):... 
    def not_by_id(self, target, *ids) -> Query(User):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(User):... 
    def not_by_name(self, target, *names) -> Query(User):... 


class UserApplicationState:
    user_id: str = str() 
    key: str = str() 
    value: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserApplicationState:... 


class UserCustomAttributeLink:
    to_entity_type: str = str() 
    from_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    user: User = User 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserCustomAttributeLink:... 


class UserCustomAttributeLinkFrom:
    to_entity_type: str = str() 
    from_entity_type: str = str() 
    configuration_id: str = str() 
    to_id: str = str() 
    user: User = User 
    configuration: CustomAttributeLinkConfiguration = CustomAttributeLinkConfiguration 
    id: str = str() 
    from_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserCustomAttributeLinkFrom:... 


class UserCustomAttributeValue:
    entity_id: str = str() 
    configuration: CustomAttributeConfiguration = CustomAttributeConfiguration 
    configuration_id: str = str() 
    value: typing.Any = None 
    key: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserCustomAttributeValue:... 


class UserSecurityRole(Entity):
    is_all_open_projects: bool = bool() 
    user_id: str = str() 
    is_all_projects: bool = bool() 
    security_role_id: str = str() 
    user_security_role_projects: UserSecurityRoleProject = UserSecurityRoleProject 
    user: User = User 
    security_role: SecurityRole = SecurityRole 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserSecurityRole:... 
    def by_id(self, target, *ids) -> Query(UserSecurityRole):... 
    def by_metadata(self, target, *dictionaries) -> Query(UserSecurityRole):... 
    def create(self) -> UserSecurityRole:... 
    def create_batch(self, *attributes) -> UserSecurityRole:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> UserSecurityRole:... 
    def get_all(self, projections=None) -> UserSecurityRole:... 
    def get_first(self, projections=None) -> UserSecurityRole:... 
    def get_inputs(self, projections=None) -> UserSecurityRole:... 
    def get_one(self, projections=None) -> UserSecurityRole:... 
    def get_outputs(self, projections=None) -> UserSecurityRole:... 
    def inject(self, filter) -> Query(UserSecurityRole):... 
    def not_by_id(self, target, *ids) -> Query(UserSecurityRole):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(UserSecurityRole):... 


class UserSecurityRoleProject(Entity):
    project: Project = Project 
    project_id: str = str() 
    user_security_role: UserSecurityRole = UserSecurityRole 
    user_security_role_id: str = str() 
    id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserSecurityRoleProject:... 
    def by_id(self, target, *ids) -> Query(UserSecurityRoleProject):... 
    def by_metadata(self, target, *dictionaries) -> Query(UserSecurityRoleProject):... 
    def create(self) -> UserSecurityRoleProject:... 
    def create_batch(self, *attributes) -> UserSecurityRoleProject:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> UserSecurityRoleProject:... 
    def get_all(self, projections=None) -> UserSecurityRoleProject:... 
    def get_first(self, projections=None) -> UserSecurityRoleProject:... 
    def get_inputs(self, projections=None) -> UserSecurityRoleProject:... 
    def get_one(self, projections=None) -> UserSecurityRoleProject:... 
    def get_outputs(self, projections=None) -> UserSecurityRoleProject:... 
    def inject(self, filter) -> Query(UserSecurityRoleProject):... 
    def not_by_id(self, target, *ids) -> Query(UserSecurityRoleProject):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(UserSecurityRoleProject):... 


class UserType:
    id: str = str() 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> UserType:... 


class UserView:
    user_id:  =  
    name: str = str() 
    global: bool = bool() 
    shared_with: Resource = Resource 
    user: User = User 
    id: str = str() 



class WorkflowSchema(Entity):
    overrides: ProjectSchemaOverride = ProjectSchemaOverride 
    id: str = str() 
    statuses: Status = Status 
    name: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> WorkflowSchema:... 
    def by_id(self, target, *ids) -> Query(WorkflowSchema):... 
    def by_metadata(self, target, *dictionaries) -> Query(WorkflowSchema):... 
    def create(self) -> WorkflowSchema:... 
    def create_batch(self, *attributes) -> WorkflowSchema:... 
    def delete(self) -> None:... 
    def from_entity_type(cls, name, ftrack_entity=None) -> typing.Any:... 
    def get(self, projections=None, limit=None, offset=0, order="ascending", order_by=None) -> WorkflowSchema:... 
    def get_all(self, projections=None) -> WorkflowSchema:... 
    def get_first(self, projections=None) -> WorkflowSchema:... 
    def get_inputs(self, projections=None) -> WorkflowSchema:... 
    def get_one(self, projections=None) -> WorkflowSchema:... 
    def get_outputs(self, projections=None) -> WorkflowSchema:... 
    def inject(self, filter) -> Query(WorkflowSchema):... 
    def not_by_id(self, target, *ids) -> Query(WorkflowSchema):... 
    def not_by_metadata(self, target, *dictionaries) -> Query(WorkflowSchema):... 


class WorkflowSchemaStatus:
    workflow_schema_id: str = str() 
    status_id: str = str() 
    Appointment: Appointment 
    Asset: Asset 
    AssetBuild: AssetBuild 
    AssetCustomAttributeLink: AssetCustomAttributeLink 
    AssetCustomAttributeLinkFrom: AssetCustomAttributeLinkFrom 
    AssetCustomAttributeValue: AssetCustomAttributeValue 
    AssetGroup: AssetGroup 
    AssetType: AssetType 
    AssetVersion: AssetVersion 
    AssetVersionCustomAttributeLink: AssetVersionCustomAttributeLink 
    AssetVersionCustomAttributeLinkFrom: AssetVersionCustomAttributeLinkFrom 
    AssetVersionCustomAttributeValue: AssetVersionCustomAttributeValue 
    AssetVersionLink: AssetVersionLink 
    AssetVersionList: AssetVersionList 
    AssetVersionStatusChange: AssetVersionStatusChange 
    CalendarEvent: CalendarEvent 
    CalendarEventResource: CalendarEventResource 
    Component: Component 
    ComponentCustomAttributeLink: ComponentCustomAttributeLink 
    ComponentCustomAttributeLinkFrom: ComponentCustomAttributeLinkFrom 
    ComponentLocation: ComponentLocation 
    ContainerComponent: ContainerComponent 
    Context: Context 
    ContextCustomAttributeLink: ContextCustomAttributeLink 
    ContextCustomAttributeLinkFrom: ContextCustomAttributeLinkFrom 
    ContextCustomAttributeValue: ContextCustomAttributeValue 
    Conversation: Conversation 
    CustomAttributeConfiguration: CustomAttributeConfiguration 
    CustomAttributeGroup: CustomAttributeGroup 
    CustomAttributeLink: CustomAttributeLink 
    CustomAttributeLinkConfiguration: CustomAttributeLinkConfiguration 
    CustomAttributeLinkFrom: CustomAttributeLinkFrom 
    CustomAttributeType: CustomAttributeType 
    CustomAttributeValue: CustomAttributeValue 
    CustomConfigurationBase: CustomConfigurationBase 
    Dashboard: Dashboard 
    DashboardResource: DashboardResource 
    DashboardWidget: DashboardWidget 
    Disk: Disk 
    Entity: Entity 
    EntitySetting: EntitySetting 
    Epic: Epic 
    Episode: Episode 
    Event: Event 
    Feed: Feed 
    FileComponent: FileComponent 
    Floor: Floor 
    Folder: Folder 
    ForwardDeclaration: ForwardDeclaration 
    Group: Group 
    GroupCustomAttributeLink: GroupCustomAttributeLink 
    GroupCustomAttributeLinkFrom: GroupCustomAttributeLinkFrom 
    Hardware: Hardware 
    Image: Image 
    Information: Information 
    Job: Job 
    JobComponent: JobComponent 
    License: License 
    List: List 
    ListCategory: ListCategory 
    ListCustomAttributeLink: ListCustomAttributeLink 
    ListCustomAttributeLinkFrom: ListCustomAttributeLinkFrom 
    ListCustomAttributeValue: ListCustomAttributeValue 
    ListObject: ListObject 
    ListObjectCustomAttributeValue: ListObjectCustomAttributeValue 
    Location: Location 
    Manager: Manager 
    ManagerType: ManagerType 
    Membership: Membership 
    Message: Message 
    Metadata: Metadata 
    Milestone: Milestone 
    Note: Note 
    NoteCategory: NoteCategory 
    NoteComponent: NoteComponent 
    NoteLabel: NoteLabel 
    NoteLabelLink: NoteLabelLink 
    ObjectType: ObjectType 
    Office: Office 
    Participant: Participant 
    Priority: Priority 
    Project: Project 
    ProjectSchema: ProjectSchema 
    ProjectSchemaObjectType: ProjectSchemaObjectType 
    ProjectSchemaOverride: ProjectSchemaOverride 
    Recipient: Recipient 
    Resource: Resource 
    Resources: Resources 
    ReviewSession: ReviewSession 
    ReviewSessionInvitee: ReviewSessionInvitee 
    ReviewSessionObject: ReviewSessionObject 
    ReviewSessionObjectStatus: ReviewSessionObjectStatus 
    Scene: Scene 
    Schema: Schema 
    SchemaStatus: SchemaStatus 
    SchemaType: SchemaType 
    Scope: Scope 
    Seat: Seat 
    SecurityRole: SecurityRole 
    Sequence: Sequence 
    SequenceComponent: SequenceComponent 
    Setting: Setting 
    SettingComponent: SettingComponent 
    Shot: Shot 
    Sprint: Sprint 
    State: State 
    Status: Status 
    StatusChange: StatusChange 
    Task: Task 
    TaskTemplate: TaskTemplate 
    TaskTemplateItem: TaskTemplateItem 
    TaskTypeSchema: TaskTypeSchema 
    TaskTypeSchemaType: TaskTypeSchemaType 
    TestTest: TestTest 
    Timelog: Timelog 
    Timer: Timer 
    Type: Type 
    TypedContext: TypedContext 
    TypedContextLink: TypedContextLink 
    TypedContextList: TypedContextList 
    TypedContextStatusChange: TypedContextStatusChange 
    User: User 
    UserApplicationState: UserApplicationState 
    UserCustomAttributeLink: UserCustomAttributeLink 
    UserCustomAttributeLinkFrom: UserCustomAttributeLinkFrom 
    UserCustomAttributeValue: UserCustomAttributeValue 
    UserSecurityRole: UserSecurityRole 
    UserSecurityRoleProject: UserSecurityRoleProject 
    UserType: UserType 
    WorkflowSchema: WorkflowSchema 
    WorkflowSchemaStatus: WorkflowSchemaStatus 

    def __init__(self, *args, **kwargs) -> None: 
    def __getitem__(self, item: typing.Union[int, slice, str]) -> WorkflowSchemaStatus:... 


